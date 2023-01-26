import rospy
import pandas as pd
import math
from datetime import time
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu, MagneticField
import time
from ekf import extended_kf
from ekf_handle import *
from geonav_conversions import *
#from states.msg import states

class States:
    def __init__(self):
        self.yaw = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.x = 0.0
        self.y = 0.0
        self.r = 0.0

class GPS:
    def __init__(self):
        self.lat = 0.0
        self.long = 0.0
        self.acc = 0.0

class IMU:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.az = 0.0
        #self.covA = [0 for i in range(9)]
        self.gx = 0.0
        self.gy = 0.0 
        self.gz = 0.0
        #self.covG = [0 for i in range(9)]

class sensor_fusion_pipeline():
    def __init__(self):
        rospy.loginfo("Hello Rita")
        self.state = States()
        self.index = 0
        self.imu = IMU()
        self.gps = GPS()

    def runAlgorithm(self):
        """ Dummy code for testing."""

        self.state_message = self.stateMsg()
        #self.imu_msg = self.messageImu()
        #self.mag_msg = self.messageMag()
        #self.index += 1

    def stateMsg(self):
        #msg = states()
        #msg.X = self.state.X
        #msg.Y = self.state.Y
        #msg.Psi = self.state.Psi
        #msg.vx = self.state.vx
        #msg.vy = self.state.vy

        #return msg
        return
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

        yaw, pitch, roll = quaternion_to_euler(x, y, z, w)
        an, ae, ad = get_accelaration(self.state.aX, self.state.aY, self.state.aZ, yaw, pitch, roll)

        # t3 = +2.0 * (w * z + x * y)
        # t4 = +1.0 - 2.0 * (y * y + z * z)
        # yaw = math.atan2(t3, t4)

        self.states.yaw = yaw
        self.states.pitch = pitch
        self.states.roll = roll
        self.states.an = an
        self.states.ae = ae
        self.states.ad = ad

        north, east, _ = LLtoUTM(data.latitude, data.longitude)
        prev_north = self.states.x
        prev_east = self.states.y
        delta_t = 0.01

        self.states.vx = (north - prev_north)/delta_t
        self.states.vy = (east - prev_east)/delta_t
        self.states.x = north
        self.states.y = east
        self.states.gps_acc = data.position_covariance

    def setIMU(self, data):
        self.imu.ax = data.linear_acceleration.x
        self.imu.ay = data.linear_acceleration.y
        self.imu.az = data.linear_acceleration.z
        self.imu.gx = data.angular_velocity.x
        self.imu.gy = data.angular_velocity.y
        self.imu.gz = data.angular_velocity.z
        self.imu.x = data.orientation.x
        self.imu.y = data.orientation.y
        self.imu.z = data.orientation.z
        self.imu.w = data.orientation.w
        # data.header.stamp 
        #self.imu.covA = data.linear_acceleration_covariance
        #self.imu.covG = data.angulr_velocity_covariance

        print('IMU')
        print('Ax = ' + str(self.imu.ax))
        print('Gx = ' + str(self.imu.gx))
        print('X  = ' + str(self.imu.x))
        print(data.header.stamp)
        print(data.linear_acceleration_covariance)
        # print(data.linear_acceleration_covariance)
        # print(data.angulr_velocity_covariance)
        return

    def setGPS(self,data):
        self.gps.lat = data.latitude
        self.gps.long = data.longitude
        self.gps.acc = data.position_covariance
        print('GPS')
        print('Lat = ' + str(self.gps.lat))
        print('Long = ' + str(self.gps.long))
        print('Acc ^ 2 = ' + str(self.gps.acc))
       
        print()
        return
        
    def setLookAhead(self, data):
        pass