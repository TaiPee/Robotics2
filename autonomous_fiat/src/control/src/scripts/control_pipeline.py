import rospy
import math
import numpy as np
import control_pid
from mymsgs.msg import control_command, car_command, states
import yaml
import matplotlib.pyplot as plt


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
        throttle_PID = control_pid.throttle_PID()
        throttle_PID.K = rospy.get_param("K")
        throttle_PID.I = rospy.get_param("I")
        lookAheadTime = rospy.get_param("look_ahead_time")
        pathToRefPath = rospy.get_param("map_dir")

        # Variables
        self.states = States()
        self.car = Car()
        controlCmd = control_command()
        carCmd = car_command()
        refPath = self.setReferencePath(pathToRefPath)
        maxSpeed = 0.0
        minSpeed = 0.0
        lookAheadTime = 0.0

    '''MAIN ALGORITHM'''

    def runAlgorithm(self):

        # Get the nearest point in the path
        index = self.getNearestIndex()

        # Get the look ahead point
        look_ahead_point = self.getLookAheadPoint(index)

        # Angle between the car and the look ahead point (ESTÁ MAL, VERIFICAR)
        alpha = math.atan2((look_ahead_point[1] - self.states.Y),(look_ahead_point[0] - self.states.X))

        # LATERAL CONTROLLER #

        # Get the steering angle
        ld = math.sqrt((look_ahead_point[1] - self.states.Y)**2 + (look_ahead_point[0] - self.states.X)**2)
        delta = math.atan((2*self.L*math.sin(alpha))/ld)

        # Get steering to messages
        self.controlCmd.steering_angle = delta
        self.carCmd.steering_angle = delta

        ## LONGITUDINAL CONTROLLER

        # Get the velocity reference
        vel_ref = self.maxSpeed - (math.exp(abs(alpha)) - 1) * (self.maxSpeed - self.minSpeed)
        self.controlCmd.velocity = vel_ref

        throttle = self.throttle_PID.calculateThrottle(vel_ref, math.sqrt(self.states.vx**2+self.states.vy**2))
        self.carCmd.throttle = throttle

    
    '''AUXILIARY FUNCTIONS'''

    def setReferencePath(self, pathToRefPath):
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

    def getLookAheadPoint(self, index):
        distance = self.lookAheadTime * math.sqrt(self.states.vx**2+self.states.vy**2)
        '''Rest of the code'''



    '''GETTERS'''

    def getControlCmd(self):
        return self.controlCmd

    def getCarCmd(self):
        return self.carCmd

    '''SETTERS'''
    
    def setStates(self, data):
        self.states.X = data.X
        self.states.Y = data.Y
        self.states.Psi = data.Psi
        self.states.vx = data.vx
        self.states.vy = data.vy
        self.states.r = data.r