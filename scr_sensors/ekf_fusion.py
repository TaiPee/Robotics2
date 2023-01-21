import rospy
import numpy as np
from ekf import extended_kf


def callback_gps(kf_north, kf_east, kf_down):

    kf_north.update()
    kf_east.update()
    kf_down.update()



def callback(kf_north, kf_east, kf_down):
    rospy.loginfo()

    kf_north.predict()
    kf_east.predict()
    kf_down.predict()

    rospy.Subscriber(callback_gps(kf_north, kf_east, kf_down))
    
    vel = np.sqrt(vel_east_predicted * vel_east_predicted + \
        vel_north_predicted * vel_north_predicted)


def fusion():
    kf_north = extended_kf()
    kf_east = extended_kf()
    kf_down = extended_kf()

    rospy.Subscriber(callback(kf_north, kf_east, kf_down))
    rospy.spin()

if __name__ == '__main__':
    fusion()