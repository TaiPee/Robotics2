#!/bin/bash

. /opt/ros/melodic/setup.bash;
. devel/setup.bash;
./src/guidance/find_path/main.py;
roslaunch mymsgs_module autonomous.launch