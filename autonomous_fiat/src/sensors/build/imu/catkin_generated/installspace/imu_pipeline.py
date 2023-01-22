import rospy
import pandas as pd
from datetime import time
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu, MagneticField

class States:
    def __init__(self):
        self.aX = 0.0
        self.aY = 0.0
        self.aZ = 0.0
        self.gX = 0.0
        self.gY = 0.0
        self.gZ = 0.0
        self.mX = 0.0
        self.mY = 0.0
        self.mZ = 0.0


class imu_pipeline():
    def __init__(self):
        rospy.loginfo("Hello Rita")
        self.states = States()
        self.index = 0

        ### For Testing Purposes
        self.accelDf, self.gyroDf, self.magnetoDf = self.readData()

    def runAlgorithm(self):
        """ Dummy code for testing."""

        ### For Testing Purposes
        self.data = []
        self.data = self.data + list(self.accelDf.loc[self.index,['x','y','z']])
        self.data = self.data + list(self.gyroDf.loc[self.index,['x','y','z']])
        self.data = self.data + list(self.magnetoDf.loc[self.index,['x','y','z']])
        ###

        self.setStates(data=self.data)
        self.imu_msg = self.messageImu()
        self.mag_msg = self.messageMag()
        self.index += 1

    def messageImu(self):

        msg = Imu()

        h = Header()
        h.stamp = rospy.Time.now()
        h.seq = self.index
        msg.header = h

        msg.orientation_covariance[0] = -1
        mat = [0.0 for i in range(9)]

        msg.linear_acceleration.x = self.states.aX
        msg.linear_acceleration.y = self.states.aY
        msg.linear_acceleration.z = self.states.aZ
        msg.linear_acceleration_covariance = mat ### Find real covariace -> TODO

        msg.angular_velocity.x = self.states.gX
        msg.angular_velocity.y = self.states.gY
        msg.angular_velocity.z = self.states.gZ
        msg.angular_velocity_covariance = mat ### Find real covariace -> TODO

        return msg

    def messageMag(self):

        msg = MagneticField()

        h = Header()
        h.stamp = rospy.Time.now()
        h.seq = self.index
        msg.header = h

        msg.magnetic_field.x = self.states.mX
        msg.magnetic_field.y = self.states.mY
        msg.magnetic_field.z = self.states.mZ

        return msg

    def getImu(self):
        return self.imu_msg

    def getMag(self):
        return self.mag_msg

    def readData(self):
        accelFile = 'accelerometer.csv'
        gyroFile = 'gyroscope.csv'
        magnetoFile = 'magnetometer.csv'

        accelDf = pd.read_csv(accelFile, sep='\t', decimal='.', lineterminator='\n', names=['timestamp','x','y','z'])
        gyroDf = pd.read_csv(gyroFile, sep='\t', decimal='.', lineterminator='\n', names=['timestamp','x','y','z'])
        magnetoDf = pd.read_csv(magnetoFile, sep='\t', decimal='.', lineterminator='\n', names=['timestamp','x','y','z'])
        
        ### GET MORE magnetic data

        magnetoDf = pd.concat([magnetoDf]*5, ignore_index=True)
        
        
        print(accelDf.shape)
        print(gyroDf.shape)
        print(magnetoDf.shape)

        return accelDf, gyroDf, magnetoDf

    def setStates(self, data):
        self.states.aX = data[0]
        self.states.aY = data[1]
        self.states.aZ = data[2]
        self.states.gX = data[3]
        self.states.gY = data[4]
        self.states.gZ = data[5]
        self.states.mX = data[6]
        self.states.mY = data[7]
        self.states.mZ = data[8]

    def setLookAhead(self, data):
        pass