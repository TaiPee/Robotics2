import rospy
import pandas as pd
from datetime import time
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu, MagneticField
import FaBo9Axis_MPU9250
import time
import sys

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


    def runAlgorithm(self):
        """ Dummy code for testing."""

        ### For Testing Purposes
        self.data = self.readData()

        self.setStates(data=self.data)
        self.imu_msg = self.messageImu()
        self.mag_msg = self.messageMag()
        self.index += 1

    def messageImu(self):

        msg = Imu()

        h = Header()
        h.stamp = rospy.Time.now()
        h.seq = self.index
        h.frame_id = 'imu_link'
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
        
        data = []
        try:
            mpu9250 = FaBo9Axis_MPU9250.MPU9250()
            accel = mpu9250.readAccel()
            
            # print( " ax = " , ( accel['x'] ))
            # print( " ay = " , ( accel['y'] ))
            # print( " az = " , ( accel['z'] ))
            # coeff_accel=[1.00047918,-0.03098151]
            #data.append(accel['x']*1.00047918-0.03098151)
            data.append(accel['x'])
            #data.append(accel['y']*0.99873312-0.01384)
            data.append(accel['y'])
            #data.append(accel['z']*0.98270031-0.06675811)
            data.append(accel['z'])

            
            gyro = mpu9250.readGyro()
            #print( " gx = " , ( gyro['x'] ))
            #print( " gy = " , ( gyro['y'] ))
            #print( " gz = " , ( gyro['z'] ))
            
            #data.append(gyro['x']-2.1239999999)
            #data.append(gyro['y']+2.0618999999)
            #data.append(gyro['z']-0.3989999999)
            data.append(gyro['x'])
            data.append(gyro['y'])
            data.append(gyro['z'])



            mag = mpu9250.readMagnet()
            #print( " mx = " , ( mag['x'] ))
            #print( " my = " , ( mag['y'] ))
            #print( " mz = " , ( mag['z'] ))
            
            data.append(mag['x']-27.6585)
            data.append(mag['y']-27.664)
            data.append(mag['z']+48.41)

            #time.sleep(0.1)
            return data
        except:
            return []
                   
        
    
    
    def setStates(self, data):
        
        if len(data)==0:
            return
            
        self.states.aX = data[0] * 9.8
        self.states.aY = data[1] * 9.8
        self.states.aZ = data[2] * 9.8
        self.states.gX = data[3] * 0.0174
        self.states.gY = data[4] * 0.0174
        self.states.gZ = data[5] * 0.0174
        self.states.mX = data[6]
        self.states.mY = data[7]
        self.states.mZ = data[8]

    def setLookAhead(self, data):
        pass
