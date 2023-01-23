from shapely.geometry import LineString
import cv2 as cv
import numpy as np
import math
from debug_plot import printWindow, drawPoints, outOfBorders

########################### IMAGE PROCESSING ###########################

def image_resize(image, area = None, inter = cv.INTER_AREA):
    """resize image to given area. If area is None, return original image"""

    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]



    # if both the width and height are None, then return the original image
    if area is None:
        return image

    r = math.sqrt(area / (w * h))
    dim = (int(w * r), int(h * r))

    # resize the image
    resized = cv.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

def getSkeleton(src):
    """get skeleton from source image. Returns a binary image"""
    grayImage = src.copy()

    # Converting to Gray Scale
    grayImage = cv.cvtColor(src,cv.COLOR_BGR2GRAY)

    # Converting to Black and White
    ret, thresholdImage = cv.threshold(grayImage,127,255,cv.THRESH_BINARY_INV)

    # obtain binary skeleton 
    sk = cv.ximgproc.thinning(thresholdImage, None, thinningType=1)  
    return sk

########################### GET RELEVANT POINTS ###########################

def neighbors(src, point, window_size=1, ordered_by_dist=False):
    """get list of neighbors of a point inside 'window_size' in a binary image. Order by distance to point"""
    neighbors = []
    for i in range(point[0] - window_size, point[0] + window_size+1):
        for j in range(point[1] - window_size, point[1] + window_size+1):
            if (    (i,j) != point  
                    and not outOfBorders(src, (i,j)) 
                    and src[i,j] == 255):
                neighbors.append((i,j))
    
    if ordered_by_dist:
        neighbors.sort(key=lambda x: math.sqrt((x[0]-point[0])**2 + (x[1]-point[1])**2))

    return neighbors

def eraseTail(original_src, point, min_tail_size):
    """check if a starting point is just a 'tail' (has a very short line) and erase it if so.
    Returns (True, source image with tail erased), or (False, original source image)"""

    src = original_src.copy()
    curr_point = point 
    tail_size = 0
    neibs = neighbors(src, curr_point)
    while tail_size < min_tail_size and len(neibs) == 1:
        src[curr_point] = 0
        curr_point = neibs[0]
        neibs = neighbors(src, curr_point)
        tail_size += 1
    
    if tail_size < min_tail_size:
        # debug
        printWindow(original_src, curr_point, text = 'before erased trail starting at ' + str(point), window_size=min_tail_size+1) 
        printWindow(src, curr_point, text = 'after erased trail starting at ' + str(point),  window_size=min_tail_size+1)
        return True, src
    else:
        return False, original_src

def getRelevantPoints(original_src, bif_window_size, min_bif_neighbors, min_tail_size):
    """get list of starting_points, bifurcation_points (each point is a tuple) from binary src image"""

    src_no_tails = original_src.copy()

    points = [tuple(p) for p in np.argwhere(src_no_tails>0)]

    # get starting points
    starting_points = []
    for point in points:
        if src_no_tails[point] and len(neighbors(src_no_tails, point)) == 1:
            # check if it's a short tail, and erase it if so
            tail_erased, src_no_tails = eraseTail(src_no_tails, point, min_tail_size)
            if not tail_erased:
                starting_points.append(point)
                printWindow(src_no_tails, point, text = 'starting point' + str(point)) # debug

    # another image to erase neib of bif points
    src = src_no_tails.copy()

    # get new points (after erasing tails)
    points = [tuple(p) for p in np.argwhere(src>0)]

    bif_points = []
    for point in points:
        # if point has more than 2 close neighbors
        if len(neighbors(src, point, window_size=1)) > 2:
            # check if has enough neighbors in window to be a bifurcation point
            if len(neighbors(src, point, window_size=bif_window_size)) >= min_bif_neighbors:
                bif_points.append(point)
                printWindow(src, point, text = 'bif point' + str(point)) # debug
    
    return starting_points, bif_points, src_no_tails

########################### DOWNSAMPLE ###########################

def downSampleCluster(cluster, tolerance):
    """downsample cluster"""

    # get cluster in shapely format
    cluster = LineString(cluster)

    # downsample cluster
    cluster = cluster.simplify(tolerance, preserve_topology=True) 
    
    # convert to list of tuples (regular format)
    cluster = [(int(x), int(y)) for (x,y) in list(cluster.coords)]

    return cluster

def downSampleClusters(clusters, max_points, initial_tolerance=1):
    """downsample clusters until """

    # add repeated points to count total points (start and end points of clusters are repeated)
    max_points += len(clusters)-1    

    # bigger tolerance = less points 
    tolerance = initial_tolerance
    total_points = np.inf

    # downsample clusters until total points is less than max_points
    while total_points > max_points and tolerance < 10:
        clusters = [downSampleCluster(cluster, tolerance) for cluster in clusters]
        total_points = sum([len(cluster) for cluster in clusters])
        tolerance += 0.2

    return clusters

########################### GET CLUSTERS ###########################

def getOrderedClusters(sk, bif_points, erase_bif_radius, min_dist_cluster, bif_window_size, min_bif_neighbors, min_tail_size):
    """get list of clusters, each a list of tuples (x,y), ordered by drawing order"""
    
    ordered_clusters = []

    # erase bif points to get the image with separate clusters 
    fig = drawPoints(sk, bif_points, color=0, radius=erase_bif_radius)

    # get starting points of figure
    starting_points, _ , fig = getRelevantPoints(fig, bif_window_size, min_bif_neighbors, min_tail_size) 

    # if there is no starting point (like a square), get all points
    if len(starting_points) == 0:
        starting_points = [ (x,y) for [x,y] in np.argwhere(fig>0) ]

    # cycle for a starting point
    for starting_point in starting_points:
        if fig[starting_point] == 0:
            continue
        
        # get the first starting point and its neighbors
        neibs = neighbors(fig, starting_point, window_size=min_dist_cluster, ordered_by_dist=True)

        # put the first point in the cluster
        ordered_cluster = [starting_point]
        curr_point = starting_point
        
        # cycle getting a cluster ('chase' the line starting at curr_point)
        while len(neibs) != 0:

            # erase curr point
            fig[curr_point] = 0

            # get next point and append it 
            curr_point = neibs[0]
            ordered_cluster.append(curr_point)

            # get new neighbors
            neibs = neighbors(fig, curr_point, window_size=min_dist_cluster, ordered_by_dist=True)
        
        ordered_clusters.append(ordered_cluster)

    return ordered_clusters    
    
########################### FILL LINES ###########################

def fillLine(a, b, min_dist):
    # Calculate the difference between the x and y coordinates of the two points
    x1, y1 = a
    x2, y2 = b

    dx = x2 - x1
    dy = y2 - y1

    for n in range(2, 5):
        # Calculate the increment in x and y needed to generate n equally spaced points along the line
        x_inc = dx / (n - 1)
        y_inc = dy / (n - 1)

        if np.linalg.norm([x_inc, y_inc]) < min_dist:
            break

    # Initialize a list to store the points
    points = []

    # Iterate over the range from 0 to n-1, generating and storing the points
    for i in range(n):
        x = x1 + i * x_inc
        y = y1 + i * y_inc
        points.append((round(x), round(y)))
    
    return points

def fillLines(points, min_dist):
    """fill lines between points with points at distance min_dist"""

    filled_points = []

    for i in range(len(points)-1):
        filled_points += fillLine(points[i], points[i+1], min_dist)
        filled_points.pop(-1)

    filled_points.append(points[-1])

    return filled_points

########################### GET START AND END POINTS ###########################

def getClosestRelevant(point, starting_points, bif_points, relevant_point_threshold):
    """if point is close to a starting point or bif point, return that point, else add it to bif points"""
    
    # get closest relevant point
    closest_relevant = np.inf
    for relevant_point in starting_points + bif_points:
        if np.linalg.norm(np.array(point)-np.array(relevant_point)) < np.linalg.norm(np.array(point)-np.array(closest_relevant)):
            closest_relevant = relevant_point
    
    # if closest relevant point is close enough, return it            
    if np.linalg.norm(np.array(point)-np.array(closest_relevant)) < relevant_point_threshold:
        return closest_relevant
    else:  
        # add point to bif points and return it 
        bif_points.append(point)
        return point

def getClosestPoints(start_point, end_point, starting_points, bif_points, sk, relevant_point_threshold):
    """get closest points in skeleton to start and end points"""    
    
    points = [(x,y) for x,y in np.argwhere(sk>0)]

    # get distances to all points
    start_distances = [np.linalg.norm(np.array(start_point)-np.array(p)) for p in points]
    end_distances = [np.linalg.norm(np.array(end_point)-np.array(p)) for p in points]

    # get closest relevant points to projected point into the path, if they are closer than 'relevant_point_threshold'
    start_point = getClosestRelevant(points[np.argmin(start_distances)], starting_points, bif_points, relevant_point_threshold)
    end_point = getClosestRelevant(points[np.argmin(end_distances)], starting_points, bif_points, relevant_point_threshold)
    
    # start_point = points[np.argmin(start_distances)]
    # end_point = points[np.argmin(end_distances)]
    
    return start_point, end_point, bif_points