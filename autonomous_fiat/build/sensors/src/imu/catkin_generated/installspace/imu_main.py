#!/usr/bin/env python2

import imu_handle
import rospy

def main():
    handle = imu_handle.imu_handle()

    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()

if __name__ == '__main__':
    main()