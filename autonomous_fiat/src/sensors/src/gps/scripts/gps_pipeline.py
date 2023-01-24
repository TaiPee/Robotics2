import rospy
import pandas as pd
from datetime import time
from std_msgs.msg import Header
from sensor_msgs.msg import NavSatFix

class States:
    def __init__(self):
        self.lat = 0.0
        self.long = 0.0
        self.accLat = 0.0
        self.accLong = 0.0


class gps_pipeline():
    def __init__(self):
        rospy.loginfo("Hello Rita")
        self.states = States()
        self.index = 0


    def runAlgorithm(self):
        """ Dummy code for testing."""

        self.data = self.readData()

        self.setStates(data=self.data)
        self.gps_msg = self.messageGps()
        self.index += 1

    def messageGps(self):

        msg = NavSatFix()

        h = Header()
        h.stamp = rospy.Time.now()
        h.seq = self.index
        h.frame_id = '/base_link'
        msg.header = h

        msg.status.service = 1
        msg.status.status = 0
        
        mat = [0.0 for i in range(9)]

        msg.latitude = self.states.lat
        msg.longitude = self.states.long

        mat[0] = self.states.accLat * self.states.accLat
        mat[3] = self.states.accLong * self.states.accLong

        msg.position_covariance = mat
        msg.position_covariance_type = 2
        return msg

  

    def getGps(self):
        return self.gps_msg

    def readData(self):
        ### TO IMPLEMENT
        # for testing purposes
        data = States()
        data.lat = 0.0
        data.long = 0.0
        data.accLat = 0.0
        data.accLong = 0.0
        ### 
        return data

    def setStates(self, data):
        self.states.lat = data.lat
        self.states.long = data.long
        self.accLat = data.accLat
        self.accLong = data.accLong