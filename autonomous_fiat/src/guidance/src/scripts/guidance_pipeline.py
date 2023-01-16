import rospy
from guidance_module.msg import point
import math

class States:
    def __init__(self):
        self.X = 0.0
        self.Y = 0.0
        self.Yaw = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.r = 0.0


class guidance_pipeline():
    def __init__(self):
        rospy.loginfo("Guidance pipeline initialized")
        self.states = States()

    def runAlgorithm(self): #! TODO
        """ Dummy code for testing."""
        vx_global = math.cos(self.Yaw)*self.vx - math.sin(self.Yaw)*self.vy
        vy_global = math.sin(self.Yaw)*self.vx + math.cos(self.Yaw)*self.vy

        self.lookahead_point = point()
        self.lookahead_point.X = self.X + vx_global
        self.lookahead_point.Y = self.Y + vy_global

    def getLookAheadPoint(self):
        return self.lookahead_point

    def setStates(self, data):
        self.states.X = data.X
        self.states.Y = data.Y
        self.states.Psi = data.Psi
        self.states.vx = data.vx
        self.states.vy = data.vy
        self.states.r = data.r
