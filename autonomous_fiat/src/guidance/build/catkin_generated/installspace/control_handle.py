import rospy
import control_pipeline
from control_module.msg import control_command, states

class control_handle():
    def __init__(self):
        rospy.init_node('control_node')
        self.pipeline = control_pipeline.control_pipeline()
        # self.subscribe()
        self.advertise()

    def subscribe(self):
        rospy.Subscriber('states_topic', states, self.statesCallback)

    def advertise(self):
        self.pubCommand = rospy.Publisher('control_cmd_topic', control_command, queue_size=1)

    def run(self):
        self.pipeline.runAlgorithm()
        control_command = self.pipeline.getControlCmd()
        self.pubCommand.publish(control_command)

    def statesCallback(self, data):
        rospy.loginfo("Received Data")
        self.pipeline.setStates(data)

        