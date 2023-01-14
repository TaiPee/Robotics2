class throttle_PID():
    def __init__(self,k,i):
        K = 10.0
        I = 0.0
    
    def calculateThrottle(self, vel_ref, vel):
        error = vel_ref - vel
        throttle = self.K*error + self.I*error