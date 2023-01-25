import rospy
import gps_pipeline
from sensor_msgs.msg import NavSatFix

class gps_handle():
    def __init__(self, api):
        rospy.init_node('imu_node')
        self.pipeline = gps_pipeline.gps_pipeline(api)
        self.advertise()

    def advertise(self):
        self.pubCommand = rospy.Publisher('gps/data', NavSatFix , queue_size=10)

    def run(self):
        self.pipeline.runAlgorithm()
        gps_msg = self.pipeline.getGps()
        self.pubCommand.publish(gps_msg)
