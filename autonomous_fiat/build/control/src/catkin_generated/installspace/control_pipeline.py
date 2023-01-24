import rospy
import math
import numpy as np
import control_pid
from mymsgs_module.msg import control_command, car_command, states
import yaml
import matplotlib.pyplot as plt
from visualization_msgs.msg import Marker
import sys
# sys.path.append('/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/guidance/')
# from find_path import main as guidance

R_MATRIX = np.array([[-2.02335264e-04,  2.32154232e-01,  4.87789686e+05],
                      [-2.32154232e-01, -2.02335264e-04,  4.28772133e+06],
                      [ 0.00000000e+00,  0.00000000e+00,  1.00000000e+00]])

class States:
    def __init__(self):
        self.X = 0.0
        self.Y = 0.0
        self.Psi = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.r = 0.0

class Car:
    def __init__(self):
        self.L = 2.46
        self.Lf = 0.74
        self.Lr = 0.6
        self.m = 1190
        self.g = 9.81
        self.Width = 1.66
        self.Length = 3.8
        self.aero_drag = 0.34
        self.r_wheel = 0.292

class control_pipeline():
    def __init__(self):
        # Configuration
        
        K = rospy.get_param("K")
        I = rospy.get_param("I")
        self.throttle_PID = control_pid.throttle_PID(K,I)

        self.simul = rospy.get_param("simul")
        if self.simul == 0:
            self.pathToRefPath = '../maps/map.yaml'
        elif self.simul == 1 or self.simul == 2:
            self.pathToRefPath = rospy.get_param("map_dir")
        else:
            rospy.logerr("Simul parameter not set correctly")

        self.lookAheadTimeLateral = rospy.get_param("look_ahead_time_lateral")
        self.lookAheadTimeLongitudinal = rospy.get_param("look_ahead_time_longitudinal")
        self.minLookAheadDist = rospy.get_param("min_look_ahead_distance")
        self.maxSpeed = rospy.get_param("max_speed")
        self.minSpeed = rospy.get_param("min_speed")
        self.k_filter_1 = rospy.get_param("k_filter_1")
        self.k_filter_2 = rospy.get_param("k_filter_2")

        # Variables
        self.states = States()
        self.car = Car()
        self.controlCmd = control_command()
        self.carCmd = car_command()
        # self.refPath = self.setReferencePath(self.pathToRefPath)
        self.refPath = None
        self.look_ahead_point_lateral_index = 0
        self.look_ahead_point_longitudinal_index = 0
        self.throttle_prev = 0.0
        


    '''MAIN ALGORITHM'''
    
    def runAlgorithm(self):

        # Get the nearest point in the path
        index = self.getNearestIndex()
        
        # Get the look ahead point
        self.look_ahead_point_lateral_index = self.getLookAheadPointIndex(index,'lateral')
        self.look_ahead_point_longitudinal_index = self.getLookAheadPointIndex(index,'longitudinal')

        # Angle between the car and the look ahead point and the distance between the 2 
        [alpha_lateral,ld_lateral] = self.getAngleAndDist(self.look_ahead_point_lateral_index) 
        [alpha_longitudinal,ld_longitudinal] = self.getAngleAndDist(self.look_ahead_point_lateral_index) 

        """ LATERAL CONTROLLER """ 
    
        # Get the steering angle according to fiat punto
        delta = np.clip(math.atan((2*self.car.L*math.sin(alpha_lateral))/ld_lateral),-0.61,0.61) #V Values from fiat punto model

        # Get steering to messages
        self.controlCmd.steering = delta
        self.carCmd.steering = delta

        """ LONGITUDINAL CONTROLLER """ 

        # Get the velocity reference
        vel_ref = self.maxSpeed - (math.exp(abs(alpha_longitudinal)) - 1) * (self.maxSpeed - self.minSpeed)
        # Guarantee end of track
        if abs(alpha_longitudinal) >= np.pi/2:
            vel_ref = 0

        self.controlCmd.velocity = vel_ref

        throttle = self.throttle_PID.calculateThrottle(vel_ref, math.sqrt(self.states.vx**2+self.states.vy**2))
        throttle = np.clip(throttle,-1.0,1.0)
        self.carCmd.throttle = throttle * self.k_filter_1 + self.throttle_prev * (1 - self.k_filter_1)

        self.throttle_prev = self.carCmd.throttle

    
    '''AUXILIARY FUNCTIONS'''

    def setReferencePath(self, pathToRefPath):
        #if self.simul == 0:
            # Execute guidance algorithm
            #guidance.main('images/tecnico_gordo.png',None,None,'world_ref',R_MATRIX)

        # Read YAML file
        with open(pathToRefPath, 'r') as file:
            points = yaml.safe_load(file)

            #Save in numpy array
            points = np.array([v for v in points['reference_path']])

        return points

    def getNearestIndex(self):
        atual_position = np.array([self.states.X, self.states.Y])

        closest_index = 0
        closest_distance = float("inf")
        
        for i, point in enumerate(self.refPath):
            distance = np.sqrt(np.power(point[0] - atual_position[0],2) + np.power(point[1] - atual_position[1],2))
            if distance < closest_distance:
                closest_index = i
                closest_distance = distance

        return closest_index
        

    def getLookAheadPointIndex(self, index, type):
        if type == 'lateral': #lateral
            ref_distance = self.lookAheadTimeLateral * math.sqrt(self.states.vx**2+self.states.vy**2)
        elif type == 'longitudinal': #longitudinal
            ref_distance = self.lookAheadTimeLongitudinal * math.sqrt(self.states.vx**2+self.states.vy**2)
        else:
            rospy.logerr("Type of look ahead point not defined")
            return -1
        ref_distance = max(ref_distance, self.minLookAheadDist)
        walking_path = 0
        final_index = len(self.refPath)-1
        pos = self.refPath[index]
        for i, point in enumerate(self.refPath[index+1:-1]):
            distance = np.sqrt(np.power(point[0] - pos[0],2) + np.power(point[1] - pos[1],2))
            pos = [point[0],point[1]]
            walking_path = walking_path + distance
            if walking_path > ref_distance:
                final_index = i + index+1
                return final_index
        return final_index

    def getAngleAndDist(self, look_ahead_point_index):
        final_index = look_ahead_point_index
        actual_pos = [self.states.X, self.states.Y]
        yaw = self.states.Psi
        yaw_normalize = [np.cos(yaw), np.sin(yaw)]
        ld = [self.refPath[final_index,0]-actual_pos[0], 
            self.refPath[final_index,1]-actual_pos[1]]
        ld_normalize = normalize(ld)

        # alpha = np.arccos(np.dot(yaw_normalize, ld_normalize))
        num = np.cross(yaw_normalize, ld_normalize)
        den = np.dot(yaw_normalize, ld_normalize)
        alpha = np.arctan2(num, den)

        distance = np.linalg.norm(ld)
        
        return [alpha,distance]

    '''VISUALIZATION FUNCTIONS'''    

    def getLookAheadMarker(self, look_ahead_point_index, type):
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.id = 1
        marker.header.stamp = rospy.Time.now()
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.a = 1.0
        marker.color.g = 0.0
        if type == 'lateral':
            marker.color.r = 1.0
            marker.color.b = 0.0
        elif type == 'longitudinal':
            marker.color.r = 0.0
            marker.color.b = 0.5
        else:
            rospy.logerr("Type of look ahead point not defined")
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = self.refPath[look_ahead_point_index,0]
        marker.pose.position.y = self.refPath[look_ahead_point_index,1]
        marker.pose.position.z = 0.0
        marker.lifetime = rospy.Duration()
        return marker

    '''GETTERS'''

    def getControlCmd(self):
        return self.controlCmd

    def getCarCmd(self):
        return self.carCmd
        
    def getLooakAheadPoint(self):
        return self.refPath(self.lookAheadPoint)

    '''SETTERS'''
    
    def setStates(self, data):
        self.states.X = data.X
        self.states.Y = data.Y
        self.states.Psi = data.Psi
        self.states.vx = data.vx
        self.states.vy = data.vy
        self.states.r = data.r



'''OTHER FUNCTIONS'''
def normalize(vector):
    norm = np.linalg.norm(vector)
    if norm == 0: 
        return vector
    return np.array(vector / norm)
