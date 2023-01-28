import rospy
import imu_pipeline
from sensor_msgs.msg import Imu, MagneticField

class imu_handle():
    def __init__(self):
        rospy.init_node('imu_node')
        self.pipeline = imu_pipeline.imu_pipeline()
        self.advertise()

    def advertise(self):
        self.pubCommandImu = rospy.Publisher('imu/data_raw', Imu , queue_size=10)
        self.pubCommandMag = rospy.Publisher('imu/mag', MagneticField , queue_size=10)

    def run(self):
        self.pipeline.runAlgorithm()
        imu_msg = self.pipeline.getImu()
        mag_msg = self.pipeline.getMag()
        self.pubCommandImu.publish(imu_msg)
        self.pubCommandMag.publish(mag_msg)
