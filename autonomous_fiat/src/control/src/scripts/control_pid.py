class throttle_PID():
    def __init__(self,k,i):
        self.error = 0
        self.error_i = 0
        self.K = k
        self.I = i
    
    def calculateThrottle(self, vel_ref, vel):
        self.error = vel_ref - vel
        self.error_i = self.error_i + self.error
        throttle = self.K*self.error + self.I*self.error_i
        return throttle