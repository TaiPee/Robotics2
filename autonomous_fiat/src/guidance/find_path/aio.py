import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math
import imageio.v2 as imageio
from random import randint
import os
from copy import deepcopy
from maps_processing.geonav_conversions import LLtoUTM

DEBUG_PRINT = False
PLOT = True
DRAW_RADIUS = 10
TEXT_SIZE = 1.2
POINTS_SIZE = 2
GIF_POINTS = 30
NO_GIF_POINTS = 150

########################### DEBUG ###########################
def outOfBorders(src, point):
    """check if point is outside the borders of the image"""
    if point[0] < 0 or point[0] >= src.shape[0] or point[1] < 0 or point[1] >= src.shape[1]:
        return True
    else:
        return False

def debugPrint(text):
    """print text if DEBUG is True"""
    if DEBUG_PRINT:
        print(text)

def printWindow(original_src, point, text=None, window_size=5):
    """print a window around a point"""
    if not DEBUG_PRINT:
        return

    src = original_src.copy()
    src[src == 255] = 1 
    src[point] = 7  

    if text is not None:
        print('\n',text,'\n')
    else:
        print('\nWindow around point: ', point)
    
    print('    ', end=' ')

    # print column numbers
    for j in range(point[1] - window_size, point[1] + window_size + 1):
        if not outOfBorders(src, (point[0], j)):
            print(f'{j:03d}', end='  ')
    print()

    # print row numbers and values
    for i in range(point[0] - window_size, point[0] + window_size + 1):
        if not outOfBorders(src, (i, point[1])):
            print('\n',f'{i:03d}', end=' ')
        for j in range(point[1] - window_size, point[1] + window_size + 1):
            if not outOfBorders(src, (i,j)):
                print(src[i,j], end='   ')
    print() 

########################### PLOTTING ###########################

# plots tiago

def plotFinalPath(path):
    plt.figure(figsize=(3, 6))
    path = np.array(path).reshape((-1,2))
    x = path[:,0]
    y = path[:,1]
    c = range(len(path))
    plt.scatter(y, -x, c=c, s=0.5)
    plt.show()

def plotClusters2(clusters):
    color = []
    cluster_list = clusters
    for i in range(len(cluster_list)):
        color.append('#%06X' % randint(0, 0xFFFFFF))
    plt.figure(figsize=(3, 6))
    #plt.scatter(curved_points[:,0], curved_points[:,1], c=labels.astype(float))
    legend_clusters = list(range(0,2*len(cluster_list),2))
    a = cluster_list[i][:][0]
    for i in range(len(cluster_list)):
        a = cluster_list[i]
        a = np.array(a).reshape(-1,2)
        plt.scatter(a[:,1], -a[:,0], s=0.5, color=color[i])
    plt.legend(legend_clusters, fontsize=5)
    plt.show()

# plots tomas

def drawPoints(src, points, color=255, radius=DRAW_RADIUS):
    """draw points on source image
    x and y ARE SWITCHED FROM 'NORMAL' POINT OF VIEW"""

    src_points = src.copy()
    # Draw the points
    if points is not None:
        for point in points:
            cv.circle(src_points, (point[1], point[0]), radius=radius, color=color, thickness=-1)
    
    return src_points

def drawLines(src, lines, color=(0,0,255), thickness=1):
    """Draw lines on source image. 
    x and y ARE SWITCHED FROM 'NORMAL' POINT OF VIEW"""
    src_lines = src.copy()
    # Draw the lines
    if lines is not None:
        for line in lines:
            cv.line(src_lines, (line[0][1], line[0][0]), (line[1][1], line[1][0]), color, thickness, cv.LINE_AA)

    return src_lines

def num_to_rgb(val, max_val=3):
    if (val > max_val):
        raise ValueError("val must not be greater than max_val")
    if (val < 0 or max_val < 0):
        raise ValueError("arguments may not be negative")

    i = (val * 255 / max_val)
    r = round(math.sin(0.024 * i + 0) * 127 + 128)
    g = round(math.sin(0.024 * i + 2) * 127 + 128)
    b = round(math.sin(0.024 * i + 4) * 127 + 128)
    return (r,g,b)

def plotClusters(clusters, shape, title=None, draw_points = False, pointRadius = DRAW_RADIUS):
    """plot image with clusters with different colors"""
    
    if not PLOT:
        return
    
    # create figure where cluster will be drawn
    fig = cv.cvtColor(np.full(shape, 255, dtype=np.uint8), cv.COLOR_GRAY2BGR)

    for color, cluster in enumerate(clusters):

        cluster = [(y,x) for (x,y) in cluster]

        # draw lines between consecutive cluster points
        for i in range(len(cluster)-1):
            cv.line(fig, cluster[i], cluster[i+1], num_to_rgb(color,len(clusters)), 3, cv.LINE_AA)

        if draw_points:
            for point in cluster:
                cv.circle(fig, point, radius=pointRadius, color=num_to_rgb(color,len(clusters)), thickness=-1)

    if title is None:
        title = str(len(clusters)) + ' Clusters'
    myPlot(fig, title)

def plotPoints(map, original_points, start_id, end_id, img_name, save_name = 'trajectory', gif = False, remove_files = True):
    """plot points on image and save trajectory as a gif."""

    
    if gif:
        n_points = GIF_POINTS
    else:
        n_points = NO_GIF_POINTS
    # downsample points for speed (if gif, even more)
    points = [original_points[i] for i in range(0, len(original_points), int(len(original_points) / n_points))]

    # plot image represented in file img_name as background in plt object
    img = cv.imread(img_name)
    plt.imshow(img)
    
    for end in map.unique_ends:
        # plot ends ids in their location
        y,x = end.location
        plt.text(x, y, end.id, color='blue')

    plt.title('Trajectory from ' + str(start_id) + ' to ' + str(end_id))

    filenames = ['original.png']
    if gif and save_name is not None:
        plt.savefig(filenames[0])

    color = 'red'
    for i,(y,x) in enumerate(points):
        filename = f'{i}.png'
        filenames.append(filename)
        # plot points with size 1
        plt.scatter( x, y, c = color, s=POINTS_SIZE)
        if gif and save_name is not None:
            plt.savefig(filename)

    if save_name is not None:
        plt.savefig(save_name + '.png')
    if PLOT:
        plt.show()

    # build gif
    if gif and save_name is not None:
        with imageio.get_writer(save_name + '.gif', mode='I') as writer:
            for filename in filenames:
                image = imageio.imread(filename)
                writer.append_data(image)         
        # remove files
        if remove_files:
            for filename in set(filenames):
                os.remove(filename)
                

    plt.close()

def myPlot(src, title, cmap='gray_r', save_name = None):
    """plot image"""

    if src is not None and PLOT:
        plt.imshow(src, cmap=cmap)
        plt.title(title)
        plt.show()
        if save_name is not None:
            plt.imsave(save_name+'.png', src, cmap=cmap)
    elif src is not None and save_name is not None:
        plt.imshow(src, cmap=cmap)
        plt.title(title)
        plt.imsave(save_name+'.png', src, cmap=cmap)

def plotRelevantPoints(sk, starting_points, bif_points, start_point, end_point):
    """plot relevant points in skeleton"""
    if not PLOT:
        return
    # draw relevant points in skeleton (get it in RGB first), and plot it
    title = str(len(starting_points)) + ' Start, ' + str(len(bif_points)) + ' Bif'
    fig = drawPoints(cv.cvtColor(255 - sk, cv.COLOR_GRAY2BGR), starting_points, color=(0,0,255), radius=DRAW_RADIUS)
    fig = drawPoints(fig, bif_points, color=(0,255,0), radius=DRAW_RADIUS)

    # draw start and end points with purple and red color
    fig = drawPoints(fig, [start_point], color=(255,0,255), radius=DRAW_RADIUS)
    fig = drawPoints(fig, [end_point], color=(0,100,0), radius=DRAW_RADIUS)
    
    myPlot(fig, title)

def plotMap(map, title = None, save_name = None):
    """plot map"""
    if not PLOT:
        return

    all_edges = deepcopy(map.edges)
    all_edges.extend(deepcopy(map.bad_edges))

    clusters = []
    shape = map.plot_shape

    # switch x and y in clusters and ends locations
    for edge in all_edges:
        edge.cluster = [(y,x) for (x,y) in edge.cluster]
        clusters.append(edge.cluster)
        for end in edge.ends:
            end.location = (end.location[1], end.location[0])

    # separate good and bad eges, good and bad clusters
    bad_edges = all_edges[len(map.edges):]
    edges = all_edges[0:len(map.edges)]
    bad_clusters = clusters[len(map.edges):]
    clusters = clusters[0:len(map.edges)]


    # create figure where cluster will be drawn
    fig = cv.cvtColor(np.full(shape, 255, dtype=np.uint8), cv.COLOR_GRAY2BGR)

    for color, cluster in enumerate(clusters):
        # draw lines between consecutive cluster points
        for i in range(len(cluster)-1):
            cv.line(fig, cluster[i], cluster[i+1], num_to_rgb(color,len(clusters)), 3, cv.LINE_AA)
    
    # draw bad clusters in gray
    color = (128,128,128)
    for cluster in bad_clusters:
        # draw lines between consecutive cluster points
        for i in range(len(cluster)-1):
            cv.line(fig, cluster[i], cluster[i+1], color, 3, cv.LINE_AA)

    # draw ends ids and edge distances
    for edge in all_edges:
        for end in edge.ends:
            # print ends ids of edge in their location
            cv.putText(fig, end.id, end.location, cv.FONT_HERSHEY_SIMPLEX, TEXT_SIZE, (0,0,0), 1, cv.LINE_AA)
        # print distance in the middle of the cluster
        middle_point = edge.cluster[len(edge.cluster)//2]
        cv.putText(fig, str(round(edge.distance)), middle_point, cv.FONT_HERSHEY_SIMPLEX, TEXT_SIZE/2, (0,0,0), 1, cv.LINE_AA)
     
    if title is None:
        title = str(len(edges)) + ' Edges, ' + str(len(bad_edges)) + ' Bad Edges (gray)'

    myPlot(fig, title, save_name = save_name)

# get points and put them in different frames

def recordClick(filename, text):
    # record click on image and return x,y coordinates with fixed axis
    image = plt.imread(filename)
    plt.title(text)
    plt.imshow(image)
    a = plt.ginput(1)
    if len(a) == 0:
        raise(Exception('No click was recorded'))
    y,x = a[0]
    
    plt.close()

    return int(round(x)), int(round(y))

# get point from image frame to world frame 
def image2world(points, image_to_world_matrix):
    points = np.array(points)

    # convert points to numpy, add extra one element, and transpose
    points = np.transpose(np.c_[points, np.ones(np.size(points,axis=0))])

    # multiply by transformation matrix and remove extra element
    real_points = np.transpose((image_to_world_matrix @ points)[:-1])

    return real_points

# get point from world frame to image frame 
def world2image(points, image_to_world_matrix):
    points = np.array(points)

    # convert points to numpy, add extra one element, and transpose
    points = np.transpose(np.c_[points, np.ones(np.size(points,axis=0))])

    # multiply by transformation matrix and remove extra element
    image_points = np.transpose((np.linalg.inv(image_to_world_matrix) @ points)[:-1])

    return image_points

# get point from current gps position 
def getGPSpoint(image_to_world_matrix):
    LLpoint = None
    
    # get gps position
    # bea e isa e tiagão
    # put them in UTM coordinates
    point = LLtoUTM(LLpoint[0], LLpoint[1])
    # put in image frame
    point = world2image(point, image_to_world_matrix)
    return point