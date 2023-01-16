#!/usr/bin/env python

import control_handle
import rospy

def main():
    handle = control_handle.control_handle()

    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()

if __name__ == '__main__':
    main()