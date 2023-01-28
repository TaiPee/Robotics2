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
WEIGHT_DATA = 0.8
WEIGHT_SMOOTH = 0.28
TOLERANCE = 0.0001
CAR_WIDTH=6
CAR_LENGTH=15
VISUALIZE = True

def get_path_vector(file_name:str)-> np.ndarray:
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

def create_binary_map(file_name: str) -> np.ndarray:
    # Load the image and convert to grayscale
    im = Image.open(file_name).convert("L")
    im_array = np.array(im)

    # Set all non-road pixels to 0
    im_array[im_array == 0] = 0

    # Set all road pixels to 1
    im_array[im_array > 0] = 1
    
    # transpose the array


    return im_array
class Car:
    def __init__(self, width: float, length: float):
        self.width = width
        self.length = length

def create_car(width: float, length: float) -> Car:
    return Car(width, length)
    path = np.array(path)
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

def get_corners(current_pos,next_pos,car):
    #initialize corners as a numpy array 4x2 
    corners = np.zeros((4,2))
    #calculate angle between current_pos and next_pos
    angle = math.atan2(next_pos[1]-current_pos[1],next_pos[0]-current_pos[0])
    
    #front right corner
    corners[0] = (current_pos[0] + (car.length/2) * math.cos(angle) + (car.width/2) * math.sin(angle), current_pos[1] + (car.length/2) * math.sin(angle) - (car.width/2) * math.cos(angle))
    #front left corner
    corners[1] = (current_pos[0] + (car.length/2) * math.cos(angle) - (car.width/2) * math.sin(angle), current_pos[1] + (car.length/2) * math.sin(angle) + (car.width/2) * math.cos(angle))
    #back right corner
    corners[2] = (current_pos[0] - (car.length/2) * math.cos(angle) + (car.width/2) * math.sin(angle), current_pos[1] - (car.length/2) * math.sin(angle) - (car.width/2) * math.cos(angle))
    #back left corner
    corners[3] = (current_pos[0] - (car.length/2) * math.cos(angle) - (car.width/2) * math.sin(angle), current_pos[1] - (car.length/2) * math.sin(angle) + (car.width/2) * math.cos(angle))
    return corners

def check_colision(path, car, binary_map):
    for i in range(len(path)-1):
        current_pos = path[i]
        next_pos = path[i+1]
        corners = get_corners(current_pos,next_pos,car)
        for corner in corners:
            if binary_map[int(corner[0])][int(corner[1])] == 0:
                return True
    
    return False

def smooth_path(path, weight_data, weight_smooth, tolerance, car, binary_map):
    
    #downsample path vector
    path = np.array(path)
    path = path[::10]
    #off_road = True
    newpath = np.array(path.copy())
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

def visualize_path(path: np.ndarray, car: Car, binary_map: np.ndarray, smooth_path: np.ndarray):
    
    # make path into a numpy array
    path = np.array(path)
    
    # #transpose the binary map
    # binary_map = np.transpose(binary_map)
    # Create figure and axis
    fig, ax = plt.subplots()
    ax.imshow(binary_map, cmap='gray')
    
    # Plot the original path
    ax.plot(path[:, 0], path[:, 1], '-o', markersize = 0.5, color='r')
    
    # Plot the smooth path
    smooth_path = np.array(smooth_path)
    ax.plot(smooth_path[:, 0], smooth_path[:, 1], markersize = 0.25, color='b')
    
    # Place the car on the path
    car_x, car_y = smooth_path[0]
    rect = Rectangle((car_x - car.length/2, car_y - car.width/2), car.length, car.width, fill=True, color='g', alpha=0.8,zorder=3)
    ax.add_patch(rect)
    
    # function to update the car position
    def update(num):
        x, y = smooth_path[num]
        rect.set_xy((x - car.length/2, y - car.width/2))
        if num < len(smooth_path) - 1:
            dx, dy = smooth_path[num + 1] - smooth_path[num]
            angle = math.degrees(math.atan2(dy, dx))
            rotate = Affine2D().rotate_deg_around(x, y, angle)
            rect.set_transform(rotate + ax.transData)
        return rect,
    ani = animation.FuncAnimation(fig, update, frames=range(len(smooth_path)), interval = 200, blit=True)
    plt.show()
    # ani.save("animation2.gif")
    # print("saved")

def smoothPathMain(path, image_name=FILE_NAME, car_width=CAR_WIDTH, car_length=CAR_LENGTH, weight_data=WEIGHT_DATA, weight_smooth=WEIGHT_SMOOTH, tolerance=TOLERANCE, visualize=VISUALIZE):
    path= np.array(path)
    path[:, [0, 1]] = path[:, [1, 0]]
    map = create_binary_map(image_name)
    my_car = create_car(car_width, car_length)
    smoothPath = smooth_path(path, weight_data, weight_smooth, tolerance, my_car, map)
    #smoothPath = check_path_limits(map, my_car.length, my_car.width, smoothPath)

    if visualize:
        visualize_path(path, my_car, map, smoothPath)
    
    return smoothPath

if __name__ == "__main__":
    path = get_path_vector(FILE_PATH)
    smoothPathMain(path)



