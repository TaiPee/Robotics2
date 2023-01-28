import yaml
import rospy
import numpy as np
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Point
import math
from tf.transformations import quaternion_from_euler
from mymsgs_module.msg import control_command, car_command, states
from sensor_msgs.msg import NavSatFix
import utm

class States:
    def __init__(self):
        self.X = self.refPath[0,0]
        self.Y = self.refPath[0,1]
        self.Psi = np.arctan2(self.refPath[1,1]-self.refPath[0,1],self.refPath[1,0]-self.refPath[0,0])
        self.vx = 0.0
        self.vy = 0.0
        self.r = 0.0

class Car:
    def __init__(self):
        self.L = rospy.get_param("car_parameters/L")
        self.Lf = rospy.get_param("car_parameters/Lf")
        self.Lr = rospy.get_param("car_parameters/Lr")
        self.m = rospy.get_param("car_parameters/m")
        self.g = rospy.get_param("car_parameters/g")
        self.Width = rospy.get_param("car_parameters/Width")
        self.Length = rospy.get_param("car_parameters/Length")
        self.aero_drag = rospy.get_param("car_parameters/aero_drag")
        self.r_wheel = rospy.get_param("car_parameters/r_wheel")
        self.MaxTorque = rospy.get_param("car_parameters/MaxTorque")
        self.GR = rospy.get_param("car_parameters/GR")
        self.eta = rospy.get_param("car_parameters/eta")

class simul_pipeline():
    def __init__(self):
        self.map_dir = rospy.get_param("map_dir")
        if self.map_dir == 0:
            self.pathToRefPath = 'map.yaml'
            self.refPath = np.array(rospy.get_param("reference_path"))
        else:
            self.pathToRefPath = self.map_dir
            self.refPath = self.setReferencePath(self.pathToRefPath)
        
        #self.pathToRefPath = '/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/guidance/find_path/images/tecnico.yaml'
        # self.refPath = self.setReferencePath()
        self.refPathVis = self.setReferencePathMarkers()
        self.carVis = Marker()
        self.carMesh = Marker()
        self.odom = states()
        self.odom.X = self.refPath[0,0]
        self.odom.Y = self.refPath[0,1]
        self.odom.Psi = np.arctan2(self.refPath[1,1]-self.refPath[0,1],self.refPath[1,0]-self.refPath[0,0])
        self.car = Car()
        self.controlCommand = control_command()
        self.carCommand = car_command()

        self.longitude = rospy.get_param("longitude")
        self.latitude = rospy.get_param("latitude")
        self.altitude = rospy.get_param("altitude")
        self.satellite = NavSatFix()
        self.satellite = self.setSatellite()
        
        

    def runSimulation(self,simul):
        if simul == 0:
            self.setSensorStates()
        elif simul == 1:
            self.setStatesAbstraction()
        elif simul == 2:
            self.setStatesThrottle()
        else:
            rospy.logerr("Simul parameter not set correctly")

        self.getCarVis()
        self.getCarMesh()

    def getCarVis(self):
        q = quaternion_from_euler(0,0,self.odom.Psi)

        self.carVis.header.frame_id = "/map"
        self.carVis.header.stamp = rospy.Time.now()
        self.carVis.type = self.carVis.CUBE
        self.carVis.id = 0
        self.carVis.action = self.carVis.ADD
        self.carVis.pose.position.x = self.odom.X - self.refPath[0,0]
        self.carVis.pose.position.y = self.odom.Y - self.refPath[0,1]
        self.carVis.pose.position.z = 0.0
        self.carVis.pose.orientation.x = q[0]
        self.carVis.pose.orientation.y = q[1]
        self.carVis.pose.orientation.z = q[2]
        self.carVis.pose.orientation.w = q[3]
        self.carVis.scale.x = self.car.Length
        self.carVis.scale.y = self.car.Width
        self.carVis.scale.z = 1
        self.carVis.color.a = 1.0
        self.carVis.color.b = 1.0
        self.carVis.lifetime = rospy.Duration()

    def setReferencePath(self):
        # Read YAML file
        with open(self.pathToRefPath, 'r') as file:
            # points = yaml.load(file, Loader=FullLoader)

            #Save in numpy array
            points = np.array([v for v in points['reference_path']])

        return points

    def setReferencePathMarkers(self):
        marker = Marker()
        marker.header.frame_id = "/map"
        marker.header.stamp = rospy.Time.now()
        marker.type = marker.LINE_STRIP # LINE_STRIP
        marker.action = marker.ADD
        marker.scale.x = 0.3
        marker.color.a = 1.0
        marker.color.g = 1.0
        marker.lifetime = rospy.Duration()
        for refPoint in self.refPath:
            point = Point()
            point.x = refPoint[0] - self.refPath[0,0]
            point.y = refPoint[1] - self.refPath[0,1]
            marker.points.append(point)

        return marker

    def getCarMesh(self):
        q = quaternion_from_euler(0,0,self.odom.Psi)

        self.carMesh.header.frame_id = "/map"
        self.carMesh.header.stamp = rospy.Time.now()
        self.carMesh.type = self.carMesh.MESH_RESOURCE
        self.carMesh.mesh_resource = "package://simulation_module/meshes/DeLorean.STL"
        self.carMesh.id = 0
        self.carMesh.action = self.carVis.ADD
        self.carMesh.pose.position.x = self.odom.X - self.refPath[0,0]
        self.carMesh.pose.position.y = self.odom.Y - self.refPath[0,1]
        self.carMesh.pose.position.z = 0.0
        self.carMesh.pose.orientation.x = q[0]
        self.carMesh.pose.orientation.y = q[1]
        self.carMesh.pose.orientation.z = q[2]
        self.carMesh.pose.orientation.w = q[3]
        # self.carMesh.scale.x = self.car.Length
        # self.carMesh.scale.y = self.car.Width
        # self.carMesh.scale.z = 1
        self.carMesh.scale.x = 1
        self.carMesh.scale.y = 1
        self.carMesh.scale.z = 1
        self.carMesh.color.a = 1.0
        self.carMesh.color.b = 1.0
        self.carMesh.lifetime = rospy.Duration()

    def setStatesThrottle(self):
        throttle = self.carCommand.throttle
        steering = self.carCommand.steering

        F = self.car.MaxTorque * 4 * self.car.GR / self.car.r_wheel * self.car.eta * throttle #- 0.5*self.car.aero_drag*(self.odom.vx**2) # Longitudinal Force

        # rospy.loginfo("F: %f",F)

        Beta = math.atan(self.car.Lr*math.tan(steering)/self.car.L) # Side Slip Angle

        integrator_step = 0.02 # For Euler Integration
        
        self.odom.X = self.odom.X + (math.sqrt(self.odom.vx**2 + self.odom.vy**2)*math.cos(self.odom.Psi+Beta)) *integrator_step
        self.odom.Y = self.odom.Y + (math.sqrt(self.odom.vx**2 + self.odom.vy**2)*math.sin(self.odom.Psi+Beta)) *integrator_step
        self.odom.Psi = self.odom.Psi + (self.odom.vx/self.car.L)*math.tan(steering) *integrator_step
        velocity = math.sqrt(self.odom.vx**2 + self.odom.vy**2) + F/self.car.m *integrator_step
        self.odom.vx = velocity*math.cos(Beta) #- 0.5*self.car.aero_drag*(self.odom.vx**2)
        self.odom.vy = velocity*math.sin(Beta)
        # rospy.loginfo('vx: %f, vy: %f',self.odom.vx, self.odom.vy)

        

    def setStatesAbstraction(self):
        velocity = self.controlCommand.velocity
        steering = self.controlCommand.steering

        Beta = math.atan(self.car.Lr*math.tan(steering)/self.car.L)

        integrator_step = 0.02
        
        self.odom.X = self.odom.X + (velocity)*math.cos(self.odom.Psi+Beta) *integrator_step
        self.odom.Y = self.odom.Y + (velocity)*math.sin(self.odom.Psi+Beta) *integrator_step
        self.odom.Psi = self.odom.Psi + (velocity*math.cos(Beta)/self.car.L)*math.tan(steering) *integrator_step
        self.odom.vx = velocity*math.cos(Beta)
        self.odom.vy = velocity*math.sin(Beta)

    def setSensorStates(self,data):
        self.odom.X = data.X
        self.odom.Y = data.Y
        self.odom.Psi = data.Psi
        self.odom.vx = data.vx
        self.odom.vy = data.vy
        self.odom.r = data.r

    def setControlCommand(self,data):
        self.controlCommand.velocity = data.velocity
        self.controlCommand.steering = data.steering

    def setCarCommand(self,data):
        self.carCommand.throttle = data.throttle
        self.carCommand.steering = data.steering

    def setSatellite(self):
        satellite = NavSatFix()

        satellite.header.frame_id = "map"
        satellite.status.status = 0
        satellite.status.service = 1
        # lat, lon = fromUTMtoLatLon(self.refPath[0,0], self.refPath[0,1],29)
        # rospy.loginfo("lat: %f, lon: %f",lat, lon)
        # satellite.latitude = lat
        # satellite.longitude = lon
        satellite.latitude = self.latitude
        satellite.longitude = self.longitude
        satellite.altitude = self.altitude
        # satellite.position_covariance = [3.9561210000000004, 0.0, 0.0, 0.0, 3.9561210000000004, 0.0, 0.0, 0.0, 7.650756]
        # satellite.position_covariance_type = 2

        return satellite

def fromUTMtoLatLon(utmX, utmY, zone):
    # Convert UTM to Lat Lon
    # https://www.programcreek.com/python/example/104280/utm.to_latlon
    lat, lon = utm.to_latlon(utmX, utmY, zone, northern=True)
    return lat, lon

    # https://tile.openstreetmap.org/${z}/${x}/${y}.png
    # https://tile.openstreetmap.org/15/995347/803458.png