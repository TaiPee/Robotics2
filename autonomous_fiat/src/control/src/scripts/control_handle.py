import rospy
import control_pipeline
from mymsgs.msg import control_command, car_command, states

class control_handle():
    def __init__(self):
        rospy.init_node('control_node')
        self.pipeline = control_pipeline.control_pipeline()
        self.subscribe()
        self.advertise()

    def subscribe(self):
        rospy.Subscriber('/states_topic', states, self.statesCallback) # Sensores
        rospy.Subscriber('/reference_path_topic', states, self.lookAheadCallback) # Look ahead de guidance

    def advertise(self):
        self.pubControlCommand = rospy.Publisher('control_cmd_topic', control_command, queue_size=1)
        self.pubCarCommand = rospy.Publisher('car_cmd_topic', car_command, queue_size=1)

    def run(self):
        self.pipeline.runAlgorithm()
        controlCmd = self.pipeline.getControlCmd()
        carCmd = self.pipeline.getCarCmd()
        self.pubCommand.publish(controlCmd)
        self.pubCommand.publish(carCmd)

    def statesCallback(self, data):
        self.pipeline.setStates(data)
        
    def lookAheadCallback(self, data):
        self.pipeline.setReferencePath(data)
        