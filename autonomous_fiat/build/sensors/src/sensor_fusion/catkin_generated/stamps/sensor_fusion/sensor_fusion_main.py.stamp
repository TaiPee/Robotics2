#!/usr/bin/env python

import sensor_fusion_handle
import rospy

def main():
    handle = sensor_fusion_handle.sensor_fusion_handle()

    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()

if __name__ == '__main__':
    main()