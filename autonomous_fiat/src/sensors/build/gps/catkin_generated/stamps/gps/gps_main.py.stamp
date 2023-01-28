#!/usr/bin/env python

import gps_handle
from pyicloud import PyiCloudService
import rospy
import time

def main():
    

    try:
        api = PyiCloudService('blourenco217@gmail.com', 'applexecDIP853')
    except KeyboardInterrupt:
        exit()

    time.sleep(5)

    handle = gps_handle.gps_handle(api)
    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()
        #time.sleep(1.0/50.0)

if __name__ == '__main__':
    main()
