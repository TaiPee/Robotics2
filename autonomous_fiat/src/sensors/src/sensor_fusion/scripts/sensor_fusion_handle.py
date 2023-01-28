import rospy
import sensor_fusion_pipeline
import matplotlib.pyplot as plt
from sensor_msgs.msg import Imu, NavSatFix
from ekf import extended_kf
import time
#from sensor_fusion_.msg import states

class sensor_fusion_handle():
    def __init__(self):
        rospy.init_node('sensor_fusion_node')
        self.pipeline = sensor_fusion_pipeline.sensor_fusion_pipeline()
        self.advertise()
        self.subscribe()


    def advertise(self):
        # self.pubStates = rospy.Publisher('/states_topic', states, queue_size=10)
        return

    def subscribe(self):
        rospy.Subscriber('/imu/data', Imu, self.imuCallback) # imu_sensor
        rospy.Subscriber('/gps/data', NavSatFix, self.gpsCallback) # gps_sensor

        
    def imuCallback(self, data):
        self.pipeline.setIMU(data)
        # Predict --->
        if self.pipeline.flag:
            self.pipeline.predict_states()

        return
    
    def gpsCallback(self, data):
        self.pipeline.setGPS(data)
        #update --->
        if self.pipeline.flag:
            self.pipeline.update_states()
        return

    def run(self):
        self.pipeline.runAlgorithm()
        
        #msg = self.pipeline.getState()
        #self.pubStates.publish(msg)