
# Introduction

Navigation systems often rely solely on Global Navigation Satellite System (GNSS) for information on position, velocity, and attitude. However, GNSS may not always be a reliable or consistent source of essential information for autonomous vehicles.

To overcome the limitations of GNSS, this work presents a sensor fusion algorithm utilizing low-cost equipment, through an Extended Kalman Filter (EKF) and a microprocessor headless implementation. This approach allows for real-time integration of information from an Inertial Measurement Unit (IMU) and a GPS module, with the use of ROS enabling seamless communication between the sensors and microprocessor. The ultimate goal is to determine the attitude, position, and speed of the vehicle with greater accuracy.

# Code organization

The code in this directory is organized into the following sub directories and files:

The current directory contains the source code for the robot.
  - `efk.py`: The main entry point for the program.


# Background

# Methodology
Qualitative comparison between GNSS and INS
|                       	| GNSS 	| INS 	|
|-----------------------	|------	|-----	|
| location              	|      	|     	|
| acquisition frequency 	|      	|     	|
| accuracy short term   	|      	|     	|



# Preliminary Results