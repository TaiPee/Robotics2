#!/usr/bin/env python

import simulation_handle as simul_handle
import rospy

def main():
    handle = simul_handle.simul_handle()

    rate = rospy.Rate(50) #50Hz
    while not rospy.is_shutdown():
        handle.run()
        rate.sleep()

if __name__ == '__main__':
    main()