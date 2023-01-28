import rospy
import numpy as np
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
import matplotlib.pyplot as plt
from gmplot import *
# from states.msg import states

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
        self.time = 0.0

class IMU:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0
        self.ax = 0.0
        self.ay = 0.0
        self.az = 0.0
        self.covA = [0 for i in range(9)]
        self.gx = 0.0
        self.gy = 0.0
        self.gz = 0.0
        self.covG = [0 for i in range(9)]
        self.time = 0.0

class sensor_fusion_pipeline():
    def __init__(self):
        rospy.loginfo("Hello Rita")
        self.states = States()
        self.index = 0
        self.gps = GPS()
        self.flag = 0
        self.imu = IMU()

        self.plot_x = []
        self.plot_y = []

        self.plot_map = True

        if self.plot_map:
            self.plot_gps_lat = []
            self.plot_gps_lon = []
            self.plot_lan = []
            self.plot_lon = []

        self.starting_time = time.time()
        

    def runAlgorithm(self):
        """ Dummy code for testing."""

        if self.flag == 0:
            time.sleep(2)
            # initialize extended kalman filter
            x, y, _ = LLtoUTM(self.gps.lat, self.gps.long)
            # x, y = latToMtrs(self.gps.lat), lonToMtrs(self.gps.long)
            self.states.x = x
            self.states.y = y
            self.kf_north = extended_kf(self.states.x, 0, self.gps.acc[0], np.sqrt( self.gps.acc[0]*self.gps.acc[0] + self.gps.acc[0]*self.gps.acc[0]), self.gps.time)
            self.kf_east = extended_kf(self.states.y, 0, self.gps.acc[3], np.sqrt( self.gps.acc[3]*self.gps.acc[3] + self.gps.acc[3]*self.gps.acc[3]), self.gps.time)

            self.prev_time = self.gps.time
            if self.states.x != 0:
                print('Kalman filter successfully initiated.')
            else:
                exit()
            self.flag = 1
        

        # print(time.time() - self.starting_time)
        if (time.time() - self.starting_time) > 143:
            # print('Performing the plot.')
            # for i in range(len(self.plot_x)):
            #     plt.scatter(self.plot_x[i], self.plot_y[i])
            #     plt.pause(0.001)

            if self.plot_map:
                print('Printing on the map')
                apikey = 'AIzaSyDHA7vBHxV3OZyOIGmMWqkz1rp7bcrRbBw'
                gmap = gmplot.GoogleMapPlotter(self.plot_lan[0], self.plot_lon[0], 18, apikey=apikey)
                gmap.scatter(self.plot_lan, self.plot_lon, color='#507af8', size=5, marker=False)
                gmap.scatter(self.plot_gps_lat, self.plot_gps_lon, color='#FF5733', size=5, marker=False)
                gmap.draw('output_maps/map.html')
                exit()
        

        # update states - position and velocity
        # self.states.x = self.kf_north.get_position()
        # self.states.y = self.kf_east.get_position()

        # self.states.vx = self.kf_north.get_velocity()
        # self.states.vy = self.kf_east.get_velocity()

        self.plot_x.append(self.states.x)
        self.plot_y.append(self.states.y)
        if self.plot_map:
            lat, lon = UTMtoLL(self.states.x, self.states.y, '29S')
            self.plot_lan.append(lat)
            self.plot_lon.append(lon)

                   
        self.state_message = self.stateMsg()
        # self.imu_msg = self.messageImu()
        # self.mag_msg = self.messageMag()
        # self.index += 1

    def stateMsg(self):
        # msg = states()
        # msg.X = self.state.X
        # msg.Y = self.state.Y
        # msg.Psi = self.state.Psi
        # msg.vx = self.state.vx
        # msg.vy = self.state.vy

        # return msg
        return

    def getState(self):
        return self.state_message
    
    def predict_states(self):
        # needed transformations
        yaw, pitch, roll = quaternion_to_euler(self.imu.x, self.imu.y, self.imu.z, self.imu.w)
        magnetic_declination = 0.02
        an, ae, ad = get_accelaration(self.imu.ax, self.imu.ay, self.imu.az, yaw + magnetic_declination, pitch, roll, self.imu.x, self.imu.y, self.imu.z, self.imu.w)

        # prediction step @ extended kalman filter
        self.kf_north.predict(an, self.imu.time)
        self.kf_east.predict(ae, self.imu.time)

        # update states - position and velocity
        self.states.x = self.kf_north.get_position()
        self.states.y = self.kf_east.get_position()

        self.states.vx = self.kf_north.get_velocity()
        self.states.vy = self.kf_east.get_velocity()

        print('acceleration', an, ae)
        print('velocity',self.states.vx, self.states.vy )

        # update states
        self.states.yaw = yaw

        self.prev_time = self.imu.time
    
    def update_states(self):
        # needed transformations
        north, east, _ = LLtoUTM(self.gps.lat, self.gps.long)

        # compute linear velocity
        delta_t = self.gps.time - self.prev_time
        delta_north = north - self.states.x
        delta_east = east - self.states.y
        v_north = delta_north/delta_t
        v_east = delta_east/delta_t

        # correction step @ extended kalman filter
        self.kf_north.update(north, v_north, self.gps.acc[0], np.sqrt( self.gps.acc[0] + self.gps.acc[0]))
        self.kf_east.update(east, v_east, self.gps.acc[3],  np.sqrt( self.gps.acc[3] + self.gps.acc[3]))


        self.prev_time = self.gps.time

        # update states - position and velocity
        self.states.x = self.kf_north.get_position()
        self.states.y = self.kf_east.get_position()

        self.states.vx = self.kf_north.get_velocity()
        self.states.vy = self.kf_east.get_velocity()

        # self.plot_x.append(self.states.x)
        # self.plot_y.append(self.states.y)
        # if self.plot_map:
        #     lat, lon = UTMtoLL(self.states.x, self.states.y, '29S')
        #     self.plot_lan.append(lat)
        #     self.plot_lon.append(lon)

        if self.plot_map:
            lat, lon = UTMtoLL(north, east, '29S')
            self.plot_gps_lat.append(lat)
            self.plot_gps_lon.append(lon)
        
        plt.scatter(self.states.x, self.states.y)
        plt.scatter(north, east, color = 'black', marker='^')
        # plt.xlim([620+4.287e6,710+4.287e6])
        # plt.ylim([473690,473760])
        plt.pause(0.0000001)
        return

    def setIMU(self, data):
        self.imu.ax = data.linear_acceleration.x
        self.imu.ay = data.linear_acceleration.y
        self.imu.az = data.linear_acceleration.z
        print('FROM IMU',self.imu.ax, self.imu.ay, self.imu.az)
        self.imu.gx = data.angular_velocity.x
        self.imu.gy = data.angular_velocity.y
        self.imu.gz = data.angular_velocity.z
        self.imu.x = data.orientation.x
        self.imu.y = data.orientation.y
        self.imu.z = data.orientation.z
        self.imu.w = data.orientation.w
        self.imu.time = data.header.stamp.to_time()
        self.covA = data.orientation_covariance
        self.covV = data.angular_velocity_covariance

    def setGPS(self,data):
        self.gps.lat = data.latitude
        self.gps.long = data.longitude
        self.gps.acc = data.position_covariance
        self.gps.time = data.header.stamp.to_time()

    def setLookAhead(self, data):
        pass