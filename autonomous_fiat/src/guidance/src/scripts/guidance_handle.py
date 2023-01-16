import rospy
import guidance_pipeline
from guidance_module.msg import point, states

class guidance_handle():
    def __init__(self):
        rospy.init_node('guidance_node')
        self.pipeline = guidance_pipeline.guidance_pipeline()
        self.subscribe()
        self.advertise()

    def subscribe(self):
        rospy.Subscriber('/states_topic', states, self.statesCallback) # Sensores
        
    def advertise(self):
        self.pubCommand = rospy.Publisher('/lookahead_topic', point, queue_size=1)

    def run(self):
        self.pipeline.runAlgorithm()
        lookahead_point = self.pipeline.getLookAheadPoint() 
        self.pubCommand.publish(lookahead_point)

    def statesCallback(self, data):
        self.pipeline.setStates(data)
        