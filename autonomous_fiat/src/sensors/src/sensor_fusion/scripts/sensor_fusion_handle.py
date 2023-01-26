import rospy
import sensor_fusion_pipeline
from sensor_msgs.msg import Imu, NavSatFix
from ekf import extended_kf
import time
#from sensor_fusion_.msg import states

class sensor_fusion_handle():
    def __init__(self):
        rospy.init_node('sensor_fusion_node')
        self.pipeline = sensor_fusion_pipeline.sensor_fusion_pipeline()
        self.advertise()
        # self.initialize_kf()
        self.subscribe()

    def advertise(self):
        # self.pubStates = rospy.Publisher('/states_topic', states, queue_size=10)
        return
    
    def init_callback(self, data, subscriber):
        self.pipeline.setGPS(data)
        self.pipeline.setIMU(data)
        subscriber.unregister()
    
    def initialize_kf(self):
        rospy.Subscriber('/imu/data', Imu, self.init_callback) # Sensores
        rospy.Subscriber('/gps/data', NavSatFix, self.init_callback) # Sensores
        self.kf_north = extended_kf(data.states.x, 0, data.states.gps_acc, data.imu_acc_n, time)
        self.kf_east = extended_kf(data.states.y, 0, data.states.gps_acc, data.imu_acc_e, time)
        return

    def subscribe(self):
        rospy.Subscriber('/imu/data', Imu, self.imuCallback) # imu_sensor
        rospy.Subscriber('/gps/data', NavSatFix, self.gpsCallback) # gps_sensor

        # get estimates from kalman filter
        predicted_x = self.kf_north.get_position()
        predicted_y = self.kf_east.get_position()

        predicted_vx = self.kf_north.get_velocity()
        predicted_vy = self.kf_east.get_velocity()

        
    def imuCallback(self, data):
        self.pipeline.setIMU(data)
        # Predict --->
        # kf_north.predict(data.states.an, time)
        # kf_east.predict(data.states.ae, time)

        return
    
    def gpsCallback(self, data):
        self.pipeline.setGPS(data)
        #update --->
        # kf_north.update(data.states.x, data.states.vx,  time)
        # kf_east.update(data.states.y, data.states.vy, time)
        return

    def run(self):
        self.pipeline.runAlgorithm()
        #msg = self.pipeline.getState()
        #self.pubStates.publish(msg)