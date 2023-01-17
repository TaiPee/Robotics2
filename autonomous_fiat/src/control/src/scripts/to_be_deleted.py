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

def plot_ref_path(points, actual_pos, idx,final_idx):
    plt.plot(points[:,0], points[:,1])
    plt.scatter(points[idx,0],points[idx,1])
    plt.scatter(points[final_idx,0],points[final_idx,1])
    plt.scatter(actual_pos[0], actual_pos[1])
    plt.show()

def closest_point(actual_pos,points):

    closest_idx = 0
    closest_distance = float("inf")
    
    for i, point in enumerate(points):
        distance = np.sqrt(np.power(point[0] - actual_pos[0],2) + np.power(point[1] - actual_pos[1],2))
        if distance < closest_distance:
            closest_idx = i
            closest_distance = distance

    return closest_idx

def look_ahead_point(points, idx, ref_distance):
    
    walking_path = 0
    final_idx = len(points)-1
    pos = points[idx]
    for i, point in enumerate(points[idx+1:-1]):
        distance = np.sqrt(np.power(point[0] - pos[0],2) + np.power(point[1] - pos[1],2))
        walking_path = walking_path + distance
        if walking_path > ref_distance:
            final_idx = i + idx+1
            return final_idx

    return final_idx



if __name__ == '__main__':
    reference_path = get_reference()
    actual_pos = np.array([4,1,np.pi]) # [x,y,orientation] [m,m,rad]
    distance = 100
    idx =  closest_point(actual_pos,reference_path)
    final_idx = look_ahead_point(reference_path, idx, distance)
    print(reference_path[idx])
    plot_ref_path(reference_path, actual_pos, idx, final_idx)



