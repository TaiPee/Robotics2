import rospy
import simulation_pipeline as simul_pipeline
from mymsgs_module.msg import control_command, car_command, states
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

class simul_handle():
    def __init__(self):
        rospy.init_node('simul_node')
        # self.simul = 1
        self.simul = rospy.get_param("simul")
        self.pipeline = simul_pipeline.simul_pipeline()
        self.advertise()
        self.subscribe()
        

    def subscribe(self):
        # rospy.Subscriber('/states_topic', states, self.statesCallback) # Sensores
        if self.simul == 1:
            rospy.Subscriber('/control_cmd_topic', control_command, self.controlCommandCallback) # Control Command - vel, steering
        elif self.simul == 2:
            rospy.Subscriber('/car_cmd_topic', car_command, self.carCommandCallback) # Car Command - throttle, steering
        elif self.simul == 0:
            rospy.Subscriber('/sensors_topics', states, self.sensorsCallback)
        else:
            rospy.logerr("Simul parameter not set correctly")


    def advertise(self):
        # Car Model
        self.pubCarStates = rospy.Publisher('simul_states_topic', states, queue_size=1)
        # Visualization
        self.pubVisCar = rospy.Publisher('Car_vis_topic', Marker, queue_size=1)
        self.pubVisRef = rospy.Publisher('refPath_vis_topic', Marker, queue_size=1)
        self.pubVisLookAhead = rospy.Publisher('lookAhead_vis_topic', Marker, queue_size=1)

    def run(self):
        self.pipeline.runSimulation(self.simul)
        # Car Model
        if self.simul!=0:
            self.pubCarStates.publish(self.pipeline.odom)
        # Visualization
        self.pubVisCar.publish(self.pipeline.carVis)
        self.pubVisRef.publish(self.pipeline.refPathVis)
        self.pubVisLookAhead.publish(self.pipeline.lookAheadVis)


    # CALLBACKS
    def controlCommandCallback(self, data):
        self.pipeline.setControlCommand(data)
        # throttle = data.throttle
        # steering = data.steering
        # self.pipeline.setStatesAbstraction(throttle, steering)

    def carCommandCallback(self, data):
        throttle = data.throttle
        steering = data.steering
        # self.pipeline.setStates(throttle, steering)

    def sensorsCallback(self, data):
        self.pipeline.setSensorStates(data)

