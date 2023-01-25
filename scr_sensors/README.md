# Introduction

Navigation systems often rely solely on Global Navigation Satellite System (GNSS) for information on position, velocity, and attitude. However, GNSS may not always be a reliable or consistent source of essential information for autonomous vehicles.

To overcome the limitations of GNSS, this work presents a sensor fusion algorithm utilizing low-cost equipment, through an Extended Kalman Filter (EKF) and a microprocessor headless implementation. This approach allows for real-time integration of information from an Inertial Measurement Unit (IMU) and a GPS module, with the use of ROS enabling seamless communication between the sensors and microprocessor (RaspberryPi). The ultimate goal is to determine the attitude, position, and speed of the vehicle with greater accuracy.

# Equipment and Tools
## Hardware
> - **Raspberry-Pi 4B**:
>  microprocessor used in this project is a low-cost, headless device that serves as the central processing unit of the system. It is responsible for running the sensor fusion algorithm and processing the data received from the IMU and GPS module.
> - **Inertial Measurement Unit (IMU):**
>  a sensor that measures the vehicle's angular velocity, linear acceleration, and magnetic field. It provides data on the vehicle's attitude, which is used in the sensor fusion algorithm.
> - **GPS module:**
> provides the vehicle's location data. It is used in conjunction with the IMU to determine the vehicle's position and speed.
## Software
> - **Ubuntu 20.04**
> - **ROS Noetic**
> is a specific version of the Robot Operating System (ROS) that is used in this project. It is an open-source software framework that enables communication between the sensors and the microprocessor. It also provides a platform for developing and testing autonomous systems.

# Code organization

The code in this directory is organized into the following sub directories and files:

  - `efk.py`: The main entry point for the program.
  - `.py`: 

# Background

Scott's videos
tutorial on how to implement an IMU using a conventional accelerometer, gyroscope, and magnetometer.
[video](https://www.youtube.com/watch?v=T9jXoG0QYIA&t=573s)

[video](https://www.youtube.com/watch?v=6M6wSLD-8M8&t=687s)

# Methodology
Qualitative comparison between GNSS and INS
|                       	| GPS(GNSS) 	| IMS(INS) 	|
|-----------------------	|--------------	|-------	|
| location              	|            	|       	|
| acquisition frequency 	|           	|       	|
| accuracy short term   	|           	|       	|



By default the library returns 3-tuple of X, Y, Z axis values for either acceleration, gyroscope and magnetometer ie compass. Default units are `m/s^2`, `rad/s`, `uT` and `°C`. It is possible to also get acceleration values in `g` and gyro values `deg/s`
# Preliminary Results
