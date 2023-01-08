import rospy
from control_module.msg import control_command

class States:
    def __init__(self):
        self.X = 0.0
        self.Y = 0.0
        self.Yaw = 0.0
        self.vx = 0.0
        self.vy = 0.0
        self.r = 0.0


class control_pipeline():
    def __init__(self):
        rospy.loginfo("Hello Rita")
        self.states = States()

    def runAlgorithm(self):
        self.control_cmd = control_command()
        self.control_cmd.throttle = self.states.vx
        self.control_cmd.steering_angle = 0.0

    def getControlCmd(self):
        return self.control_cmd

    def setStates(self, data):
        self.states.X = data.X
        self.states.Y = data.Y
        self.states.Yaw = data.Yaw
        self.states.vx = data.vx
        self.states.vy = data.vy
        self.states.r = data.r