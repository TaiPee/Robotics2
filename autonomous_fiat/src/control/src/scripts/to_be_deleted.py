import math
import yaml
import numpy as np
import matplotlib.pyplot as plt

def read_matrix_from_yaml(filepath):
    with open(filepath, 'r') as file:
        matrix = yaml.safe_load(file)
    return matrix

def get_reference():
    points = read_matrix_from_yaml("/home/rita/Robotics/Robotics2/autonomous_fiat/src/control/src/maps/reference_path.yaml")
    points = np.array([v for v in points['reference_path']])

    return points

def plot_ref_path(points):
    plt.plot(points[:,0], points[:,1])
    plt.show()

def closest_point(atual_position,points):

    closest_index = 0
    closest_distance = float("inf")
    
    for i, point in enumerate(points):
        distance = np.sqrt(np.power(point[0] - atual_position[0],2) + np.power(point[1] - atual_position[1],2))
        if distance < closest_distance:
            closest_index = i
            closest_distance = distance
    print(points[closest_index])

    return closest_index

def look_ahead_point(points, index, ref_distance):
    
    walking_path = 0
    final_index = len(points)-1
    pos = points[index]
    for i, point in enumerate(points[index+1:-1]):
        distance = np.sqrt(np.power(point[0] - pos[0],2) + np.power(point[1] - pos[1],2))
        walking_path = walking_path + distance
        if walking_path > ref_distance:
            final_index = i + index+1
            return final_index

    return final_index



if __name__ == '__main__':
    reference_path = get_reference()
    actual_position = np.array([4,1])
    distance = 2
    index =  closest_point(actual_position)
    final_index = look_ahead_point(reference_path, index, distance)


