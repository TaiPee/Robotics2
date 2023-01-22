import rospy
import sensor_fusion_pipeline
from sensor_msgs.msg import Imu

class sensor_fusion_handle():
    def __init__(self):
        rospy.init_node('sensor_fusion_node')
        self.pipeline = sensor_fusion_pipeline.sensor_fusion_pipeline()
        self.advertise()
        self.subscribe()

    def advertise(self):
        return

    def subscribe(self):
        rospy.Subscriber('/imu/data', Imu, self.imuCallback) # Sensores
        
    def imuCallback(self, data):
        self.pipeline.setStates(data)
        return

    def run(self):
        self.pipeline.runAlgorithm()