# %%

import cv2 as cv
import image as img
import search as srch

# advise to set PLOT to True in debug_plot.py to visualize results of the pipeline
import debug_plot as dbg 

# define start and end point for each image in images, if None, will be asked in the image
START_POINTS = [(277, 556), None, None, None] # must be SAME SIZE as IMAGES
END_POINTS = [(719, 142), None, None, None] # must be SAME SIZE as IMAGES

# list images available
FILENAMES = ['images/tecnico.jpg', 'images/path1.jpg' , 'images/path2.png', 'images/path3.jpg']

# INDEXES OF IMAGES IN FILENAMES TO PROCESS
TO_PROCESS = [1]

FILENAMES = [FILENAMES[i] for i in TO_PROCESS]    
START_POINTS = [START_POINTS[i] for i in TO_PROCESS]
END_POINTS = [END_POINTS[i] for i in TO_PROCESS]

############################################################################################
#########     sections of the code and hyperparameters of each section:    #################
############################################################################################

##########   IMAGE PROCESSING   ##########

# Resize

AREA = None # area of the resized image - None to keep original size

# Get relevant points

MIN_TAIL_SIZE = 10 # tails that are shorter than MIN_TAIL_SIZE will be removed
BIF_WINDOW_SIZE = 7 # bif points have 3+ direct neibs, AND more than MIN_BIF_NEIGHBORS inside BIF_WINDOW_SIZE 
MIN_BIF_NEIGHBORS = BIF_WINDOW_SIZE*3 # avoid considering edges as bifurcation points

# Get clusters

ERASE_BIF_RADIUS = 3 # points that are closer than ERASE_BIF_RADIUS of a bifurcation point will be erased
MIN_DIST_CLUSTER = 2 # sort cluster window: minimum distance between 2 points of the same cluster

##########   SEARCH    ##########

INTER_CLUSTER_DIST = 9 # maximum distance between 2 clusters to be considered neighbors

########################### MAIN ###########################

def main(start_points=None, end_points=None, filenames=None):

    # allow to call main with just one image
    if not isinstance(start_points, list):
        start_points = [start_points]
    if not isinstance(end_points, list):
        end_points = [end_points]
    if not isinstance(filenames, list):
        filenames = [filenames]

    # process images in filenames
    for start_point, end_point, filename in zip(start_points, end_points, filenames):
        dbg.debugPrint('Processing ' + filename)

        ##########   GET START AND END POINTS (IF NOT PROVIDED) ##########
        if start_point is None:
            start_point = dbg.recordClick(filename, 'Click on start point')
        if end_point is None:
            end_point = dbg.recordClick(filename, 'Click on end point')

        ##########   IMAGE PROCESSING   ##########

        # Reading and recizing image
        src = img.image_resize(cv.imread(filename), area=AREA)

        # get skeleton from source image
        sk = img.getSkeleton(src)

        # get closest point in path to start and end
        start_point, end_point = img.getClosestPoint(start_point, end_point , sk)

        # get starting and bifurcation points, erase short tails
        starting_points, bif_points, sk = img.getRelevantPoints(sk, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, MIN_TAIL_SIZE)
        bif_points = bif_points + [start_point, end_point]
        dbg.plotRelevantPoints(sk, starting_points, bif_points, start_point, end_point)

        # get clusters with ordered points
        clusters = img.getOrderedClusters(sk, bif_points, ERASE_BIF_RADIUS, MIN_DIST_CLUSTER, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, MIN_TAIL_SIZE)
        # dbg.plotClusters(clusters, sk.shape, 'Clusters (' + str(len(clusters)) + ')' ) 
        
        ##########   SEARCH    ##########

        map = srch.Map(clusters, INTER_CLUSTER_DIST, sk.shape)
        # dbg.plotClusters([edge.cluster for edge in map.edges], sk.shape, 'Fixed clusters (' + str(len(fixed_clusters)) + ')' ) 
        # dbg.plotMap(map)

        # get start and end ids from map.unique_ends that are closest to start_point and end_point
        start, end = srch.getStartEndIDs(map,start_point, end_point)

        path = srch.a_star(map.graph, start, end)
        points = srch.getPointsFromPath(path, map)
        dbg.plotPoints(map, points, start, end, filename, save_name=filename.split('.')[0]+'_path', gif = True)

        ########## SAVE .TXT ##########
            
        # save x and y coordinates of clusters in txt file in main folder
        with open(filename.split('.')[0] + '.txt', 'w') as f:
            for x,y in points:
                f.write(str(x) + ' ' + str(y) + '\n') 
        
             
if __name__ == "__main__":
    main(START_POINTS, END_POINTS, FILENAMES)

# %%