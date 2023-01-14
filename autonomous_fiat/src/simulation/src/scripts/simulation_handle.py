import rospy
import sumulation_pipeline as simul_pipeline
from mymsgs.msg import control_command, car_command, states
from visualization_msgs import Marker
from visualization_msgs import MarkerArray


class control_handle():
    def __init__(self):
        rospy.init_node('simul_node')
        self.pipeline = simul_pipeline.simul_pipeline()
        self.subscribe()
        self.advertise()

    def subscribe(self):
        # rospy.Subscriber('/states_topic', states, self.statesCallback) # Sensores
        rospy.Subscriber('/control_cmd_topic', control_command, self.controlCommandCallback) # Control Command - vel, steering
        rospy.Subscriber('/car_cmd_topic', car_command, self.carCommandCallback) # Car Command - throttle, steering

    def advertise(self):
        self.pubVisCar = rospy.Publisher('refPath_vis_topic', Marker, queue_size=1)
        self.pubVisRef = rospy.Publisher('refPath_vis_topic', MarkerArray, queue_size=1)

    def run(self):
        self.pipeline.runSimulation()

        self.pubVisCar.publish()


    # CALLBACKS
    def controlCommandCallback(self, data):
        pass

    def carCommandCallback(self, data):
        pass