#!/usr/bin/env python

import guidance_handle
import rospy

def main():
    handle = guidance_handle.guidance_handle()

    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()

if __name__ == '__main__':
    main()