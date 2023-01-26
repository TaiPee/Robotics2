import rospy
import sensor_fusion_pipeline
from sensor_msgs.msg import Imu, NavSatFix
#from sensor_fusion_.msg import states

class sensor_fusion_handle():
    def __init__(self):
        rospy.init_node('sensor_fusion_node')
        self.pipeline = sensor_fusion_pipeline.sensor_fusion_pipeline()
        self.advertise()
        self.subscribe()

    def advertise(self):
        #self.pubStates = rospy.Publisher('/states_topic', states, queue_size=10)
        return

    def subscribe(self):
        rospy.Subscriber('/imu/data', Imu, self.imuCallback) # Sensores
        rospy.Subscriber('/gps/data', NavSatFix, self.gpsCallback) # Sensores
        
    def imuCallback(self, data):
        self.pipeline.setIMU(data)
        #Predict --->
        return
    
    def gpsCallback(self, data):
        self.pipeline.setGPS(data)
        #update --->
        return

    def run(self):
        self.pipeline.runAlgorithm()
        #msg = self.pipeline.getState()
        #self.pubStates.publish(msg)