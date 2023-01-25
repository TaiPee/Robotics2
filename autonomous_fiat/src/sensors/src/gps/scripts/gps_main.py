#!/usr/bin/env python

import gps_handle
from pyicloud import PyiCloudService
import rospy

def main():
    handle = gps_handle.gps_handle()

    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()

if __name__ == '__main__':
    main()