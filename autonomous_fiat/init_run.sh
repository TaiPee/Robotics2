#!/bin/bash

. /opt/ros/melodic/setup.bash;
. devel/setup.bash;
./src/guidance/main.py;
roslaunch mymsgs_module autonomous.launch
