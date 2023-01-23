import rospy
import math
import control_pipeline
from mymsgs_module.msg import control_command, car_command, states
from visualization_msgs.msg import Marker
from std_msgs.msg import Float32

class control_handle():
    def __init__(self):
        rospy.init_node('control_node')
        self.simul = rospy.get_param("simul")
        self.pipeline = control_pipeline.control_pipeline()
        self.firstSensorRead = False
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

        self.pubVelocity = rospy.Publisher('/velocity_vis_topic', Float32, queue_size=1)
        self.pubThrottle = rospy.Publisher('/throttle_vis_topic', Float32, queue_size=1)
        self.pubSteeringAngle = rospy.Publisher('/steeringAngle_vis_topic', Float32, queue_size=1)

    def run(self):
        if self.firstSensorRead == True:
            self.pipeline.runAlgorithm()
            controlCmd = self.pipeline.getControlCmd()
            carCmd = self.pipeline.getCarCmd()
            lookAheadLateralMarker = self.pipeline.getLookAheadMarker(self.pipeline.look_ahead_point_lateral_index,'lateral')
            lookAheadLongitudinalMarker = self.pipeline.getLookAheadMarker(self.pipeline.look_ahead_point_longitudinal_index,'longitudinal')
            self.pubControlCommand.publish(controlCmd)
            self.pubCarCommand.publish(carCmd)

            #Visualization
            self.pubLooKAheadLateralVis.publish(lookAheadLateralMarker)
            self.pubLooKAheadLongitudinalVis.publish(lookAheadLongitudinalMarker)
            self.pubVelocity.publish(math.sqrt(self.pipeline.states.vx**2+self.pipeline.states.vy**2))
            self.pubThrottle.publish(self.pipeline.carCmd.throttle)
            self.pubSteeringAngle.publish(self.pipeline.controlCmd.steering)

    def statesCallback(self, data):
        self.pipeline.setStates(data)

        # If first time execute guidance algorithm
        if self.firstSensorRead == False:
            self.pipeline.refPath = self.pipeline.setReferencePath(self.pipeline.pathToRefPath)
            self.firstSensorRead = True

        
    def lookAheadCallback(self, data):
        self.pipeline.setReferencePath(data)
        