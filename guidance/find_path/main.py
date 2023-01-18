# %%

import cv2 as cv
import numpy as np
import search as srch
import image as img
import my_search as my_srch

# advise to set PLOT to True in debug_plot.py to visualize results of the pipeline
import debug_plot as dbg 

# list images available
IMAGES = ['images/path1.jpg' , 'images/path2.png', 'images/tecnico.jpg']

# index of images to to process inside IMAGES list (can process multiple images at once)
IM_NUM = [2]
PROCESS_IMG_NAMES = [IMAGES[i] for i in IM_NUM]    

############################################################################################
#########     sections of the code and hyperparameters of each section:    #################
############################################################################################

##########   IMAGE PROCESSING   ##########

# Resize

AREA = 600*1200 # area of the resized image - None to keep original size

# Get relevant points

MIN_TAIL_SIZE = 10 # tails that are shorter than MIN_TAIL_SIZE will be removed
BIF_WINDOW_SIZE = 7 # bif points have 3+ direct neibs, AND more than MIN_BIF_NEIGHBORS inside BIF_WINDOW_SIZE 
MIN_BIF_NEIGHBORS = BIF_WINDOW_SIZE*3 # avoid considering edges as bifurcation points

# Get clusters

ERASE_BIF_RADIUS = 3 # points that are closer than ERASE_BIF_RADIUS of a bifurcation point will be erased
MIN_DIST_CLUSTER = 2 # sort cluster window: minimum distance between 2 points of the same cluster

# Downsampling

MAX_POINTS = 50 # max number of points to give the robot

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

        map = my_srch.Map(clusters, INTER_CLUSTER_DIST, sk.shape)
        fixed_clusters = [edge.cluster for edge in map.edges]
        # dbg.plotClusters(fixed_clusters, sk.shape, 'Fixed clusters (' + str(len(fixed_clusters)) + ')' ) 
        dbg.plotMap(map)

        start = map.unique_ends[0].id
        end = map.unique_ends[-1].id
        path = my_srch.a_star(map.graph, start, end)
        print(path)                
        dbg.plotPath(path, map)


        ########## SAVE .TXT TO PASS TO THE ROBOT ##########
            
        # save x and y coordinates of clusters in txt file in main folder
        # with open(filename.split('/')[-1].split('.')[0] + '.txt', 'w') as f:
        #     for x,y in points:
        #         y = sk.shape[1] - y
        #         x,y = round(x*SCALE), round(y*SCALE)
        #         f.write(str(y) + ' ' + str(x) + '\n') 
        
        # plot results
        # dbg.plotPoints(points, sk, gifname=filename.split('/')[-1].split('.')[0])
             
if __name__ == "__main__":
    main()

# %%