import rospy
import pandas as pd
from datetime import time
from std_msgs.msg import Header
from sensor_msgs.msg import NavSatFix
import time
from pyicloud import PyiCloudService
from geonav_conversions import *
import matplotlib.pyplot as plt

class States:
    def __init__(self):
        self.lat = 0.0
        self.long = 0.0
        self.posCov = 0.0


class gps_pipeline():
    def __init__(self, api):
        rospy.loginfo("Hello Rita")
        self.api = api
        self.device = self.api.devices[1]
        self.states = States()
        self.index = 0
        self.current_ts = 0


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

        mat[0] = self.states.posCov
        mat[3] = self.states.posCov

        msg.position_covariance = mat
        msg.position_covariance_type = 2
        return msg

  

    def getGps(self):
        return self.gps_msg

    def readData(self):
        ### TO IMPLEMENT
        # for testing purposes
        data = States()
        location = self.device.location()
        
        if location['positionType'] == 'GPS' and location['timeStamp'] != self.current_ts:
            print(location['latitude'], location['longitude'])
            print(location['horizontalAccuracy'])
            self.current_ts = location['timeStamp']
            #lat = location['latitude']
            #lon = location['longitude']
            #north, east, _ = LLtoUTM(lat, lon)
            data.lat = location['latitude']
            data.long = location['longitude']
            data.posCov = location['horizontalAccuracy'] * location['horizontalAccuracy']
            return data

        return self.data

    def setStates(self, data):
        self.states.lat = data.lat
        self.states.long = data.long
        self.states.posCov = data.posCov