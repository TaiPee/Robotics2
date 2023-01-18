# %%

import cv2 as cv
import image as img
import my_search as srch
import numpy as np

# advise to set PLOT to True in debug_plot.py to visualize results of the pipeline
import debug_plot as dbg 

# list images available
IMAGES = ['images/tecnico.jpg', 'images/path1.jpg' , 'images/path2.png', 'images/path3.jpg']

# index of images to to process inside IMAGES list (can process multiple images at once)
IM_NUM = [0,1,2,3]
PROCESS_IMG_NAMES = [IMAGES[i] for i in IM_NUM]    

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

# Downsampling

MAX_POINTS = 30 # max number of points to give the robot

# Fill lines 

FILL_LINES = True # fill lines or not
AVG_DIST_F = 2 # fill line with points if distance between points is more than AVG_DIST_F*avg_dist

SCALE = 1 # scale of the image to draw

##########   SEARCH    ##########

INTER_CLUSTER_DIST = 9 # maximum distance between 2 clusters to be considered neighbors

########################### MAIN ###########################

def main ():

    # process images in filenames
    for filename in PROCESS_IMG_NAMES:

        ##########   IMAGE PROCESSING   ##########

        # Reading and recizing image
        src = img.image_resize(cv.imread(filename), area=AREA)

        # get skeleton from source image
        sk = img.getSkeleton(src)

        # get starting and bifurcation points, erase short tails
        starting_points, bif_points, sk = img.getRelevantPoints(sk, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, MIN_TAIL_SIZE)
        # dbg.plotRelevantPoints(sk, starting_points=starting_points, bif_points=bif_points)

        # get clusters with ordered points
        clusters = img.getOrderedClusters(sk, bif_points, ERASE_BIF_RADIUS, MIN_DIST_CLUSTER, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, MIN_TAIL_SIZE)

        ##########   SEARCH    ##########

        map = srch.Map(clusters, INTER_CLUSTER_DIST, sk.shape)
        # dbg.plotClusters([edge.cluster for edge in map.edges], sk.shape, 'Fixed clusters (' + str(len(fixed_clusters)) + ')' ) 
        dbg.plotMap(map)

        # 'A' - 'U' in tecnico map
        start = map.unique_ends[0].id
        end = map.unique_ends[-1].id
        path = srch.a_star(map.graph, start, end)
        points = srch.getPointsFromPath(path, map)
        
        # avg distance between points using numpy
        dbg.plotPoints(map, points, start, end, filename, save_name=filename.split('.')[0])

        ########## SAVE .TXT ##########
            
        # save x and y coordinates of clusters in txt file in main folder
        with open(filename.split('.')[0] + '.txt', 'w') as f:
            for x,y in points:
                f.write(str(x) + ' ' + str(y) + '\n') 
        
             
if __name__ == "__main__":
    main()

# %%