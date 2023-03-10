import rospy
import control_pipeline
from mymsgs_module.msg import control_command, car_command, states
from visualization_msgs.msg import Marker

class control_handle():
    def __init__(self):
        rospy.init_node('control_node')
        self.simul = rospy.get_param("simul")
        self.pipeline = control_pipeline.control_pipeline()
        self.subscribe()
        self.advertise()
        self.lookAheadMarker = Marker()

    def subscribe(self):
        if self.simul == 0:
            rospy.Subscriber('/states_topic', states, self.statesCallback) # Sensores
        elif self.simul == 1 or self.simul == 2:
            rospy.Subscriber('/simul_states_topic', states, self.statesCallback) # Simulation

    def advertise(self):
        # CONTROL
        self.pubControlCommand = rospy.Publisher('/control_cmd_topic', control_command, queue_size=1)
        self.pubCarCommand = rospy.Publisher('/car_cmd_topic', car_command, queue_size=1)
        # VISUALIZATION
        self.pubLooKAheadLateralVis = rospy.Publisher('/lookAheadLateral_vis_topic', Marker, queue_size=1)
        self.pubLooKAheadLongitudinalVis = rospy.Publisher('/lookAheadLongitudinal_vis_topic', Marker, queue_size=1)

    def run(self):
        self.pipeline.runAlgorithm()
        controlCmd = self.pipeline.getControlCmd()
        carCmd = self.pipeline.getCarCmd()
        lookAheadLateralMarker = self.pipeline.getLookAheadMarker(self.pipeline.look_ahead_point_lateral_index,'lateral')
        lookAheadLongitudinalMarker = self.pipeline.getLookAheadMarker(self.pipeline.look_ahead_point_longitudinal_index,'longitudinal')
        self.pubControlCommand.publish(controlCmd)
        self.pubCarCommand.publish(carCmd)
        self.pubLooKAheadLateralVis.publish(lookAheadLateralMarker)
        self.pubLooKAheadLongitudinalVis.publish(lookAheadLongitudinalMarker)

    def statesCallback(self, data):
        self.pipeline.setStates(data)
        
    def lookAheadCallback(self, data):
        self.pipeline.setReferencePath(data)
        