import numpy as np
from typing import Tuple
from scipy.interpolate import splprep, splev
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
from matplotlib.patches import Rectangle
from matplotlib.transforms import Affine2D
import math

# Parameters used in case you want to run this script as a standalone
FILE_NAME = "images/tecnico_1280.png"
FILE_PATH = "images/tecnico_1280.txt"
WEIGHT_DATA = 0.1
WEIGHT_SMOOTH = 0.1
TOLERANCE = 0.00001
CAR_WIDTH=1
CAR_HEIGHT=1
VISUALIZE = True

def get_path_vector(file_name):
    # Load the data from the .txt file
    path_data = np.loadtxt(file_name)

    # Get the x and y coordinates
    x_coords = path_data[:, 0]
    y_coords = path_data[:, 1]

    # Create a path vector of points
    path_vector = np.column_stack((x_coords, y_coords))
    
    # downsample path vector
    downsample_path = path_vector[::20]

    return downsample_path

def create_binary_map(file_name):
    # Load the image and convert to grayscale
    im = Image.open(file_name).convert("L")
    im_array = np.array(im)

    # Set all non-road pixels to 0
    im_array[im_array < 255] = 0

    # Set all road pixels to 1
    im_array[im_array == 255] = 1
    
    # transpose the array
    im_array = np.transpose(im_array)

    return im_array

class Car:
    def __init__(self, width, length):
        self.width = width
        self.length = length

def create_car(width, length):
    return Car(width, length)

def smooth_path(path, weight_data, weight_smooth, tolerance):
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]
    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(1, len(path)-1):
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += weight_smooth * (newpath[i-1][j] + newpath[i+1][j] - (2.0 * newpath[i][j]))
                change += abs(aux - newpath[i][j])
    return newpath

def check_path_limits(binary_map, car_length, car_width, smooth_path):
    for i in range(1, len(smooth_path)):
        #len(smooth_path)-2
        current_position = smooth_path[i-1]
        next_position = smooth_path[i]
        
        def get_corners(current_position,next_position):
            # calculate angle between current position and next position
            angle = math.atan2(next_position[1] - current_position[1], next_position[0] - current_position[0])
            
            # calculate the four corners of the car based on angle and car length and width
            #front right corner
            corner1 = (current_position[0] + (car_length/2) * math.cos(angle) - (car_width/2) * math.sin(angle), current_position[1] + (car_length/2) * math.sin(angle) + (car_width/2) * math.cos(angle))
            #back right corner
            corner2 = (current_position[0] - (car_length/2) * math.cos(angle) - (car_width/2) * math.sin(angle), current_position[1] - (car_length/2) * math.sin(angle) + (car_width/2) * math.cos(angle))
            #front left corner
            corner3 = (current_position[0] + (car_length/2) * math.cos(angle) + (car_width/2) * math.sin(angle), current_position[1] + (car_length/2) * math.sin(angle) - (car_width/2) * math.cos(angle))
            #back left corner
            corner4 = (current_position[0] - (car_length/2) * math.cos(angle) + (car_width/2) * math.sin(angle), current_position[1] - (car_length/2) * math.sin(angle) - (car_width/2) * math.cos(angle))
            #get the two sides coordinates of the car
            
            return [corner1, corner2, corner3, corner4, angle]
    
        # get the four corners of the car
        corner1, corner2, corner3, corner4, angle = get_corners(current_position,next_position)
        
        # 1st check if any of the corners of the car are off road
        count = 0
        off_road = False
        for corner in [corner1, corner2, corner3, corner4]:
            if binary_map[int(corner[1]), int(corner[0])] == 0:
                off_road = True
                count += 1
        # if all corners are off road, move to next position
        if count == 4:
            #NAO SEI O QUE FAZER AQUI
            count = 4
        
        # if off road, correct position until within road limits
        if not off_road:
            continue
        
        # loop through the four corners of the car
        nCorner = 0
        for corner in [corner1, corner2, corner3, corner4]:
            nCorner += 1
            # if corner is off road, move it back towards the center of the car
            if binary_map[int(corner[1]), int(corner[0])] == 1:
                continue
            # move the center towards the opposite left or right side of the car
            if nCorner < 3:
                # move the center towards the left side of the car
                current_position = (current_position[0] + 1 * math.cos(angle), current_position[1] + 1 * math.sin(angle))
                break
            else:
                #move the center towards the right side of the car
                current_position = (current_position[0] - 1 * math.cos(angle), current_position[1] - 1 * math.sin(angle))
                break
        # save the new position
        smooth_path[i-1] = current_position
        i=i-1
                        
                    
                    
                    
                
                
    return smooth_path

def visualize_path(path, car, binary_map, smooth_path):
        
    # make path into a numpy array
    path = np.array(path)
    
    # #transpose the binary map
    # binary_map = np.transpose(binary_map)
    # Create figure and axis
    fig, ax = plt.subplots()
    ax.imshow(binary_map, cmap='gray')
    
    # Plot the original path
    ax.plot(path[:, 0], path[:, 1], '-o', markersize = 2, color='r')
    
    # Plot the smooth path
    smooth_path = np.array(smooth_path)
    ax.plot(smooth_path[:, 0], smooth_path[:, 1], markersize = 1, color='b')
    
    # Place the car on the path
    car_x, car_y = smooth_path[0]
    rect = Rectangle((car_x - car.width/2, car_y - car.length/2), car.width, car.length, fill=True, color='g', alpha=0.5)
    ax.add_patch(rect)
    
    # function to update the car position
    def update(num):
        x, y = smooth_path[num]
        rect.set_xy((x - car.width/2, y - car.length/2))
        if num < len(smooth_path) - 1:
            dx, dy = smooth_path[num + 1] - smooth_path[num]
            angle = math.degrees(math.atan2(dy, dx))
            rotate = Affine2D().rotate_deg_around(x, y, angle)
            rect.set_transform(rotate + ax.transData)
        return rect,
    ani = animation.FuncAnimation(fig, update, frames=range(len(smooth_path)), interval = 200, blit=True)
    plt.show()
    #ani.save("animation.gif")
    # print("saved")

def smoothPathMain(path, image_name=FILE_NAME, car_width=CAR_WIDTH, car_height=CAR_HEIGHT, weight_data=WEIGHT_DATA, weight_smooth=WEIGHT_SMOOTH, tolerance=TOLERANCE, visualize=VISUALIZE):
    map = create_binary_map(image_name)
    my_car = create_car(car_width, car_height)
    smoothPath = smooth_path(path, weight_data, weight_smooth, tolerance)
    smoothPath = check_path_limits(map, my_car.length, my_car.width, smoothPath)

    if visualize:
        visualize_path(path, my_car, map, smoothPath)
    
    return smoothPath

if __name__ == "__main__":
    path = get_path_vector(FILE_PATH)
    smoothPathMain(path)



