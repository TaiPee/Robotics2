import rospy
import pandas as pd
import math
from datetime import time
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu, MagneticField

class States:
    def __init__(self):
        self.yaw = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.x = 0.0
        self.y = 0.0
        self.r = 0.0

class sensor_fusion_pipeline():
    def __init__(self):
        rospy.loginfo("Hello Rita")
        self.states = States()
        self.index = 0

        ### For Testing Purposes
        #self.accelDf, self.gyroDf, self.magnetoDf = self.readData()

    def runAlgorithm(self):
        """ Dummy code for testing."""

        print(self.states.yaw)
        #self.imu_msg = self.messageImu()
        #self.mag_msg = self.messageMag()
        #self.index += 1

    def readData(self):
        return

    def setStates(self, data):
        self.states.aX = data.linear_acceleration.x
        self.states.aY = data.linear_acceleration.y
        self.states.aZ = data.linear_acceleration.z
        
        x = data.orientation.x
        y = data.orientation.y
        z = data.orientation.z
        w = data.orientation.w

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw = math.atan2(t3, t4)

        self.states.yaw = yaw
        self.states.vx = 0.0
        self.states.vy = 0.0
        self.states.vz = 0.0
        self.states.x = 0.0
        self.states.x = 0.0
        self.states.y = 0.0
        self.states.z = 0.0


    def setLookAhead(self, data):
        pass