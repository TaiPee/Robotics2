""" 
Robotics course at Instituto Superior Tecnico, 2022/2023
Laboratory 2 - Autonomous Driving 

Code developed by the GUIDANCE team of Group ?:
 
Bernardo Carvalho, 
Rafael Jeronimo, 93163
Tomás Líbano Monteiro, 93196
"""

import cv2 as cv
import aio as io
import image as img
import search as srch
import smooth_path as smth
import numpy as np

############################################################################################
############     CHANGE PARAMETERS BELLOW TO RUN SCRIPT DIRECTLY:    #######################
############################################################################################

# define start and end point for each image in images (in image coord), if None, will be asked in the image
START_POINTS = [(487902.91516208043, 4287516.813179664), None, None, None] 
END_POINTS = [(488004.4493165874, 4287611.675840042), None, None, None] 

# transformation matrices from image frame to inertial frame (real world frame) 
R_MATRIX = [np.array([[-2.02335264e-04,  2.32154232e-01,  4.87789570e+05],
                      [-2.32154232e-01, -2.02335264e-04,  4.28772144e+06],
                      [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]), 
            
            np.array([[-2.02335264e-04,  2.32154232e-01,  4.87789570e+05],
                      [-2.32154232e-01, -2.02335264e-04,  4.28772144e+06],
                      [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]]), 
            None, 
            None] 

# list images available
FILENAMES = ['images/tecnico.png', 'images/tecnico_gordo.png' , 'images/path2.png', 'images/path3.jpg']
FILENAMES_FILLED = ['images/tecnico_gordo.png', 'images/tecnico_gordo.png' , 'images/path2.png', 'images/path3.jpg']

# Indexes of images in filenames list TO ACTUALLY PROCESS
TO_PROCESS = [0]

############################################################################################
######################     HYPERPARAMETERS OF THE CODE     #################################
############################################################################################

# image.py

MIN_TAIL_SIZE = 5 # tails that are shorter than MIN_TAIL_SIZE will be removed
BIF_WINDOW_SIZE = 7 # bif points have 3+ direct neibs, AND more than MIN_BIF_NEIGHBORS inside BIF_WINDOW_SIZE 
MIN_BIF_NEIGHBORS = BIF_WINDOW_SIZE*3 # avoid considering edges as bifurcation points
RELEVANT_POINT_THRESHOLD = 30 # if choosen start or end point is closer than this to a relevant points, will merge with them
ERASE_BIF_RADIUS = 3 # points that are closer than ERASE_BIF_RADIUS of a bifurcation point will be erased
MIN_DIST_CLUSTER = 2 # sort cluster window: minimum distance between 2 points of the same cluster

# search.py

INTER_CLUSTER_DIST = 20 # maximum distance between 2 clusters to be considered neighbors

# debug_plot.py

GIF = True # if True, will save a gif of the process, if False, will only save an image of the final result

############################################################################################
################################     MAIN     ##############################################
############################################################################################

def main(filename, filename_filled, start_point, end_point, points_ref, r_matrix = None):

    ##########   GET START AND END POINTS IN IMAGE FRAME ##########
    if points_ref != 'world_ref' and points_ref != 'image_ref':
        raise Exception('Invalid points reference, must be "world_ref" or "image_ref"')

    if start_point is None:
        start_point = io.recordClick(filename, 'Click on start point')
    elif points_ref == 'world_ref':
        start_point = io.world2image(start_point, r_matrix)
    if end_point is None:
        end_point = io.recordClick(filename, 'Click on end point')
    elif points_ref == 'world_ref':
        end_point = io.world2image(end_point, r_matrix)
        
    ##########   IMAGE PROCESSING   ##########

    # reading and resizing image
    src = img.image_resize(cv.imread(filename), area=None)

    # get skeleton from source image
    sk = img.getSkeleton(src)

    # get starting and bifurcation points, erase short tails
    starting_points, bif_points, sk = img.getRelevantPoints(sk, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, MIN_TAIL_SIZE)
    
    # get closest point in path to start and end, and update bif points if necessary
    start_point, end_point, bif_points = img.getClosestPoints(start_point, end_point, starting_points, bif_points, sk, RELEVANT_POINT_THRESHOLD)
    io.plotRelevantPoints(sk, starting_points, bif_points, start_point, end_point)

    # get clusters with ordered points
    clusters = img.getOrderedClusters(sk, bif_points, ERASE_BIF_RADIUS, MIN_DIST_CLUSTER, BIF_WINDOW_SIZE, MIN_BIF_NEIGHBORS, 4)
    
    ##########   SEARCH    ##########

    map = srch.Map(clusters, INTER_CLUSTER_DIST, sk.shape)
    # io.plotClusters([edge.cluster for edge in map.edges], sk.shape, 'Fixed clusters (' + str(len(fixed_clusters)) + ')' ) 
    io.plotMap(map)

    # get start and end ids from map.unique_ends that are closest to start_point and end_point
    start, end = srch.getStartEndIDs(map,start_point, end_point)

    path = srch.a_star(map.graph, start, end)
    if path is None:
        print('No path found')
        return None
        
    points = srch.getPointsFromPath(path, map)
    io.plotPoints(map, points, start, end, filename, save_name=filename.split('.')[0]+'_path', gif = GIF)

    ##########   SMOOTH PATH    ##########
    
    points = smth.smoothPathMain(points, filename_filled)

    ########## CHANGE COORDINATES AND SAVE TO FILE ##########

    points_UTM_frame = dbg.image2world(points, r_matrix)
    
    # write yaml file
    with open(filename.split('.')[0] + '.yaml', 'w') as f:
        string = 'reference_path: '+ str([[x,y] for x,y in points_UTM_frame])
        f.write(string.replace('],', '],\n'))

    with open('map.yaml', 'w') as f:
        string = 'reference_path: '+ str([[x,y] for x,y in points_UTM_frame])
        f.write(string.replace('],', '],\n'))

    # write txt file (image frame) for comparison
    with open(filename.split('.')[0] + '.txt', 'w') as f:
        for x,y in points:
            f.write(str(x) + ' ' + str(y) + '\n') 

    return points_UTM_frame

def testScript():
    """ This function is used to test the script. It will run the main function with the global variables set in this script. """
    # update lists with indexes to process
    filenames = [FILENAMES[i] for i in TO_PROCESS] 
    filenames_filled = [FILENAMES_FILLED[i] for i in TO_PROCESS] 
    start_points = [START_POINTS[i] for i in TO_PROCESS]
    end_points = [END_POINTS[i] for i in TO_PROCESS]
    r_matrices = [R_MATRIX[i] for i in TO_PROCESS]
    
    if len(start_points) != len(end_points) or len(start_points) != len(filenames):
        raise ValueError('start_points, end_points and filenames must be lists of the same size')
    
    # run main function for each image
    for filename, filename_filled, start_point, end_point, r_matrix in zip(filenames, filenames_filled, start_points, end_points, r_matrices):
        print('Processing ' + filename)
        main(filename, filename_filled, start_point, end_point, points_ref = 'world_ref', r_matrix = r_matrix)
        
if __name__ == "__main__":
    testScript()