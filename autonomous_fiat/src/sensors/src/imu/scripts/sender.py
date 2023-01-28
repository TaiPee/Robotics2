import rospy
import pandas as pd
import numpy as np
from datetime import time
from std_msgs.msg import Header
from geometry_msgs.msg import Quaternion, Vector3
from sensor_msgs.msg import Imu, MagneticField

def talker(accelDf, gyroDf, magnetoDf):
    pub = rospy.Publisher('imu/data_raw', Imu , queue_size=10)
    pub2 = rospy.Publisher('imu/mag', MagneticField , queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        msg = messageImuFiller(i,accelDf['timestamp'][i],accelDf.loc[i,['x','y','z']], gyroDf.loc[i,['x','y','z']])
        msg2 = messageMagFiller(i, magnetoDf['timestamp'][i],magnetoDf.loc[i,['x','y','z']])
        rospy.loginfo(msg)
        rospy.loginfo(msg2)
        pub.publish(msg)
        pub2.publish(msg2)
        rate.sleep()
        i += 1

def messageImuFiller(i, timestamp, a, g):

    msg = Imu()

    h = Header()
    h.stamp = rospy.Time.now()
    h.seq = i
    msg.header = h

    msg.orientation_covariance[0] = -1
    mat = [0.0 for i in range(9)]

    msg.linear_acceleration.x = a[0]
    msg.linear_acceleration.y = a[1]
    msg.linear_acceleration.z = a[2]
    msg.linear_acceleration_covariance = mat

    msg.angular_velocity.x = g[0]
    msg.angular_velocity.y = g[1]
    msg.angular_velocity.z = g[2]
    msg.angular_velocity_covariance = mat

    return msg

def messageMagFiller(i, timestamp, m):

    msg = MagneticField()

    h = Header()
    h.stamp = rospy.Time.now()
    h.seq = i
    msg.header = h

    msg.magnetic_field.x = m[0]
    msg.magnetic_field.y = m[1]
    msg.magnetic_field.z = m[2]

    return msg
def readFiles():

    accelFile = 'src/imu/scripts/accelerometer.csv'
    gyroFile = 'src/imu/scripts/gyroscope.csv'
    magnetoFile = 'src/imu/scripts/magnetometer.csv'

    accelDf = pd.read_csv(accelFile, sep='\t', decimal='.', lineterminator='\n', names=['timestamp','x','y','z'])
    gyroDf = pd.read_csv(gyroFile, sep='\t', decimal='.', lineterminator='\n', names=['timestamp','x','y','z'])
    magnetoDf = pd.read_csv(magnetoFile, sep='\t', decimal='.', lineterminator='\n', names=['timestamp','x','y','z'])
    print(accelDf.shape)
    print(gyroDf.shape)
    print(magnetoDf.shape)

    return accelDf, gyroDf, magnetoDf
if __name__ == '__main__':
    try:
        accelDf, gyroDf, magnetoDf = readFiles()
        talker(accelDf, gyroDf, magnetoDf)
    except rospy.ROSInterruptException:
        pass