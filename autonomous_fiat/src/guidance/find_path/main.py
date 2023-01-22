""" 
Robotics course at Instituto Superior Tecnico, 2022/2023
Laboratory 2 - Autonomous Driving 

Code developed by GUIDANCE team of Group ?:
 
Bernardo Carvalho, 
Rafael Jeronimo,
Tomás Líbano Monteiro, 93196
"""

import cv2 as cv
import image as img
import search as srch
import numpy as np
import debug_plot as dbg 

############################################################################################
########################     CHANGE PARAMETERS BELLOW:    ##################################
############################################################################################

# define start and end point for each image in images, if None, will be asked in the image
START_POINTS = [None, None, None, None] 
END_POINTS = [None, None, None, None] 

# transformation matrices from image frame to inertial frame (real world frame) 
R_MATRIX = [None, 
            np.array([[-0.018623413997238, 0.231812495281406, -1.320596088340964e+02], 
                     [-0.231812495281406, -0.018623413997238, 63.803816354536260],
                     [0, 0, 1]]), 
            None, 
            None] 

# list images available
FILENAMES = ['images/tecnico.jpg', 'images/tecnico_1280.png' , 'images/path2.png', 'images/path3.jpg', 'images/path3.jpg']

# Indexes of images in filenames list TO ACTUALLY PROCESS
TO_PROCESS = [0,1,2,3]

############################################################################################
#########     SECTIONS OF THE CODE AND HYPERPARAMETERS OF EACH SECTION     #################
############################################################################################

# Get relevant points

MIN_TAIL_SIZE = 5 # tails that are shorter than MIN_TAIL_SIZE will be removed
BIF_WINDOW_SIZE = 7 # bif points have 3+ direct neibs, AND more than MIN_BIF_NEIGHBORS inside BIF_WINDOW_SIZE 
MIN_BIF_NEIGHBORS = BIF_WINDOW_SIZE*3 # avoid considering edges as bifurcation points
RELEVANT_POINT_THRESHOLD = 30 # if choosen start or end point is closer than this to a relevant points, will merge with them

# Get clusters

ERASE_BIF_RADIUS = 3 # points that are closer than ERASE_BIF_RADIUS of a bifurcation point will be erased
MIN_DIST_CLUSTER = 2 # sort cluster window: minimum distance between 2 points of the same cluster

# Search path

INTER_CLUSTER_DIST = 8 # maximum distance between 2 clusters to be considered neighbors

############################################################################################
################################     MAIN     ##############################################
############################################################################################

# update lists with indexes to process
FILENAMES = [FILENAMES[i] for i in TO_PROCESS]    
START_POINTS = [START_POINTS[i] for i in TO_PROCESS]
END_POINTS = [END_POINTS[i] for i in TO_PROCESS]
R_MATRIX = [R_MATRIX[i] for i in TO_PROCESS]

def main(start_points=None, end_points=None, filenames=None, default_values=False):
    """ Can call this function with other scripts. If default_values is True, will use default 
    values for start_points, end_points and filenames set in global variables FILENAME, START_POINTS and END_POINTS.
    Otherwise, will use the ones provided. start_points, end_points and filenames must be lists of the same size."""

    if default_values == True:
        # use default values
        start_points = START_POINTS
        end_points = END_POINTS
        filenames = FILENAMES
        r_matrices = R_MATRIX
    else:
        # allow to call main with just one image
        if not isinstance(start_points, list):
            start_points = [start_points]
        if not isinstance(end_points, list):
            end_points = [end_points]
        if not isinstance(filenames, list):
            filenames = [filenames]
        if not isinstance(r_matrices, list):
            r_matrices = [r_matrices]
        if len(start_points) != len(end_points) or len(start_points) != len(filenames):
            raise ValueError('start_points, end_points and filenames must be lists of the same size')

    # process images in filenames
    for start_point, end_point, filename, r_matrix in zip(start_points, end_points, filenames, r_matrices):
        print('Processing ' + filename)

        ##########   GET START AND END POINTS (IF NOT PROVIDED) ##########
        if start_point is None:
            start_point = dbg.recordClick(filename, 'Click on start point')
        if end_point is None:
            end_point = dbg.recordClick(filename, 'Click on end point')

        ##########   IMAGE PROCESSING   ##########

        # reading and resizing image
        src = img.image_resize(cv.imread(filename), area=None)

        # get skeleton from source image
        sk = img.getSkeleton(src)

        # get starting and bifurcation points, erase short tails
        starting_points, bif_points, sk = img.getRelevantPoints(sk, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, MIN_TAIL_SIZE)
        
        # get closest point in path to start and end, and update bif points if necessary
        start_point, end_point, bif_points = img.getClosestPoints(start_point, end_point, starting_points, bif_points, sk, RELEVANT_POINT_THRESHOLD)
        dbg.plotRelevantPoints(sk, starting_points, bif_points, start_point, end_point)

        # get clusters with ordered points
        clusters = img.getOrderedClusters(sk, bif_points, ERASE_BIF_RADIUS, MIN_DIST_CLUSTER, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, 4)
        # dbg.plotClusters(clusters, sk.shape, 'Clusters (' + str(len(clusters)) + ')' ) 
        
        ##########   SEARCH    ##########

        map = srch.Map(clusters, INTER_CLUSTER_DIST, sk.shape)
        # dbg.plotClusters([edge.cluster for edge in map.edges], sk.shape, 'Fixed clusters (' + str(len(fixed_clusters)) + ')' ) 
        dbg.plotMap(map)

        # get start and end ids from map.unique_ends that are closest to start_point and end_point
        start, end = srch.getStartEndIDs(map,start_point, end_point)

        path = srch.a_star(map.graph, start, end)
        if path is None:
            print('     No path found',)
            continue
        else:
            print('     Path:', path)
        points = srch.getPointsFromPath(path, map)
        dbg.plotPoints(map, points, start, end, filename, save_name=filename.split('.')[0]+'_path', gif = True)

        ########## CHANGE COORDINATES ##########
        
        # convert to numpy, add extra one element, and transpose
        with open(filename.split('.')[0] + '.yaml', 'w') as f:
            # convert points to numpy, add extra one element, and transpose
            points_np = np.transpose(np.c_[np.array(points), np.ones(len(points))])

            # multiply by transformation matrix and remove extra element
            if r_matrix is None:
                r_matrix = np.eye(3)
            real_points = np.transpose((r_matrix @ points_np)[:-1])

            # write yaml file
            string = 'reference_path: '+ str([[x,y] for x,y in real_points])
            f.write(string.replace('],', '],\n'))

        # write txt file (image frame)
        with open(filename.split('.')[0] + '.txt', 'w') as f:
            for x,y in points:
                f.write(str(x) + ' ' + str(y) + '\n') 
             
if __name__ == "__main__":
    main(default_values=True)