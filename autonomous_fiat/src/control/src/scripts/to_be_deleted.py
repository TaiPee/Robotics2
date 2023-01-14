import math
import yaml
import numpy as np
import matplotlib.pyplot as plt


def read_matrix_from_yaml(filepath):
    with open(filepath, 'r') as file:
        matrix = yaml.safe_load(file)
    return matrix

def plot_ref_path(points):
    plt.plot(points[:,0], points[:,1])
    plt.show()


def closest_point():

    points = read_matrix_from_yaml("/home/rita/Robotics/Robotics2/autonomous_fiat/src/control/src/maps/reference_path.yaml")
    points = np.array([v for v in points['reference_path']])
    atual_position = np.array([4,1])

    closest_index = 0
    closest_distance = float("inf")
    
    for i, point in enumerate(points):
        distance = np.sqrt(np.power(point[0] - atual_position[0],2) + np.power(point[1] - atual_position[1],2))
        if distance < closest_distance:
            closest_index = i
            closest_distance = distance
    print(points[closest_index])

    return closest_index


if __name__ == '__main__':
    closest_point()