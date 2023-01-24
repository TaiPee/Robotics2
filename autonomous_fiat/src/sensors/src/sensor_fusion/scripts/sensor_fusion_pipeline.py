import rospy
import pandas as pd
import math
from datetime import time
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu, MagneticField
from states.msg import states

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
        self.state = States()
        self.index = 0

    def runAlgorithm(self):
        """ Dummy code for testing."""

        print(self.state.yaw)
        self.state_message = self.stateMsg()
        #self.imu_msg = self.messageImu()
        #self.mag_msg = self.messageMag()
        #self.index += 1

    def stateMsg(self):
        msg = states()
        msg.X = self.state.X
        msg.Y = self.state.Y
        msg.Psi = self.state.Psi
        msg.vx = self.state.vx
        msg.vy = self.state.vy

        return msg
    
    def getState(self):
        return self.state_message

    def setStates(self, data):
        self.state.aX = data.linear_acceleration.x
        self.state.aY = data.linear_acceleration.y
        self.state.aZ = data.linear_acceleration.z
        
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
        self.states.x = 0.0
        self.states.y = 0.0


    def setLookAhead(self, data):
        pass