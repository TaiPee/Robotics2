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
<<<<<<< Updated upstream
        rospy.loginfo("Hello Rita")
        self.states = States()

    def runAlgorithm(self):
        """ Dummy code for testing."""
        self.control_cmd = control_command()
        self.control_cmd.throttle = self.states.vx
        self.control_cmd.steering_angle = 0.0
=======
        # Configuration
        K = rospy.get_param("K")
        I = rospy.get_param("I")
        self.throttle_PID = control_pid.throttle_PID(K,I)
        self.maxSpeed = rospy.get_param("max_speed")
        self.minSpeed = rospy.get_param("min_speed")
        self.lookAheadTimeLateral = rospy.get_param("look_ahead_time_lateral")
        self.lookAheadTimeLongitudinal = rospy.get_param("look_ahead_time_longitudinal")
        self.look_ahead_point_lateral_index = 0
        self.look_ahead_point_longitudinal_index = 0

        
        # Variables
        self.states = States()
        self.car = Car()
        self.controlCmd = control_command()
        self.carCmd = car_command()
        self.pathToRefPath = rospy.get_param("map_dir")
        self.refPath = self.setReferencePath(self.pathToRefPath)

    '''MAIN ALGORITHM'''

    def runAlgorithm(self):

        # Get the nearest point in the path
        index = self.getNearestIndex()

        # Get the look ahead lateral point 
        self.look_ahead_point_lateral_index = self.getLookAheadPointIndex(index,True)
        self.look_ahead_point_longitudinal_index = self.getLookAheadPointIndex(index,False)


        # Angle between the car and the look ahead point and the distance between the 2 
        [alpha,ld] = self.getAngleAndDist() 

        # LATERAL CONTROLLER #

        # Get the steering angle
        delta = math.atan((2*self.car.L*math.sin(alpha))/ld)

        # Get steering to messages
        self.controlCmd.steering = delta
        self.carCmd.steering = delta

        ## LONGITUDINAL CONTROLLER

        # Get the velocity reference
        vel_ref = self.maxSpeed - (math.exp(abs(alpha)) - 1) * (self.maxSpeed - self.minSpeed)
        rospy.loginfo("Velocity %f",vel_ref)
        self.controlCmd.velocity = vel_ref

        throttle = self.throttle_PID.calculateThrottle(vel_ref, math.sqrt(self.states.vx**2+self.states.vy**2))
        self.carCmd.throttle = throttle

    
    '''AUXILIARY FUNCTIONS'''

    def setReferencePath(self, pathToRefPath):
        # Read YAML file
        with open(pathToRefPath, 'r') as file:
            points = yaml.safe_load(file)

            #Save in numpy array
            points = np.array([v for v in points['reference_path']])

        return points

    def getNearestIndex(self):
        atual_position = np.array([self.states.X, self.states.Y])

        closest_index = 0
        closest_distance = float("inf")
        
        for i, point in enumerate(self.refPath):
            distance = np.sqrt(np.power(point[0] - atual_position[0],2) + np.power(point[1] - atual_position[1],2))
            if distance < closest_distance:
                closest_index = i
                closest_distance = distance

        return closest_index
        

    def getLookAheadPointIndex(self, index, type):
        if type: #lateral
            ref_distance = self.lookAheadTimeLateral * math.sqrt(self.states.vx**2+self.states.vy**2)
        else:
            ref_distance = self.lookAheadTimeLongitudinal * math.sqrt(self.states.vx**2+self.states.vy**2)

        walking_path = 0
        final_index = len(self.refPath)-1
        pos = self.refPath[index]
        for i, point in enumerate(self.refPath[index+1:-1]):
            distance = np.sqrt(np.power(point[0] - pos[0],2) + np.power(point[1] - pos[1],2))
            pos = [point[0],point[1]]
            walking_path = walking_path + distance
            if walking_path > ref_distance:
                final_index = i + index+1
                return final_index
        return final_index

    def getAngleAndDist(self):
        final_index = self.look_ahead_point_index
        actual_pos = [self.states.X, self.states.Y]
        yaw = self.states.Psi
        yaw_normalize = [np.cos(yaw), np.sin(yaw)]
        ld = [self.refPath[final_index,0]-actual_pos[0], 
            self.refPath[final_index,1]-actual_pos[1]]
        ld_normalize = normalize(ld)
        alpha = np.arccos(np.dot(yaw_normalize, ld_normalize))
        distance = np.linalg.norm(ld)
        
        return [alpha,distance]

    '''VISUALIZATION FUNCTIONS'''    

    def getLookAheadMarker(self):
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.id = 1
        marker.header.stamp = rospy.Time.now()
        marker.type = marker.SPHERE
        marker.action = marker.ADD
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.5
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.pose.orientation.w = 1.0
        marker.pose.position.x = self.refPath[self.look_ahead_point_index,0]
        marker.pose.position.y = self.refPath[self.look_ahead_point_index,1]
        marker.pose.position.z = 0.0
        marker.lifetime = rospy.Duration()
        return marker

    '''GETTERS'''
>>>>>>> Stashed changes

    def getControlCmd(self):
        return self.control_cmd

    def setStates(self, data):
        self.states.X = data.X
        self.states.Y = data.Y
        self.states.Psi = data.Psi
        self.states.vx = data.vx
        self.states.vy = data.vy
        self.states.r = data.r

    def setLookAhead(self, data):
        pass