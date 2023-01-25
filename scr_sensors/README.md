# Introduction

Navigation systems often rely solely on Global Navigation Satellite System (GNSS) for information on position, velocity, and attitude. However, GNSS may not always be a reliable or consistent source of essential information for autonomous vehicles.

To overcome the limitations of GNSS, this work presents a sensor fusion algorithm utilizing low-cost equipment, through an Extended Kalman Filter (EKF) and a microprocessor headless implementation. This approach allows for real-time integration of information from an Inertial Measurement Unit (IMU) and a GPS module, with the use of ROS enabling seamless communication between the sensors and microprocessor (RaspberryPi). The ultimate goal is to determine the attitude, position, and speed of the vehicle with greater accuracy.

# Equipment and Tools
## Hardware
> - **Raspberry-Pi 4B:**
>  microprocessor used in this project is a low-cost, headless device that serves as the central processing unit of the system. It is responsible for running the sensor fusion algorithm and processing the data received from the IMU and GPS module.
> - **Inertial Measurement Unit (IMU):**
>  a sensor that measures the vehicle's angular velocity, linear acceleration, and magnetic field. It provides data on the vehicle's attitude, which is used in the sensor fusion algorithm.
> - **GPS module:**
> provides the vehicle's location data. It is used in conjunction with the IMU to determine the vehicle's position and speed.
## Software
> - **Ubuntu 20.04**
> - **ROS Noetic**
> is a specific version of the Robot Operating System (ROS) that is used in this project. It is an open-source software framework that enables communication between the sensors and the microprocessor. It also provides a platform for deploying and testing the system.

# Code organization

The code in this directory is organized into the following sub directories and files:

  - `efk.py`: The main entry point for the program.
  - `.py`: 

# Background



### Inputs (Make sure IMU fixed in NED frame)
1) Latitude, units are `rad`
2) Longitude, units are `rad`
3) Altitude, units are `m`
4) Velocity (North), units are `m/s`
5) Velocity (East), units are `m/s`
6) Velocity (Down), units are `m/s`
7) Accelarometer X, units are `m/s^2`
8) Accelarometer Y, units are `m/s^2`
9) Accelarometer Z, units are `m/s^2`
10) Gyro X, units are `rad/s`
11) Gyro Y, units are `rad/s`
12) Gyro Z, units are `rad/s`
13) Magnetometer X, units need to be consistant across all magnetometer measurements used (eg. mT)
14) Magnetometer Y, units need to be consistant across all magnetometer measurements used (eg. mT)
15) Magnetometer Z, units need to be consistant across all magnetometer measurements used (eg. mT)

With an objective of enhancing the accuracy of GPS readings based on IMU reading an Extended Kalman Filter (EKF) was implemented.
## Extended Kalman Filter
EKF to fuse GPS, IMU and encoder readings to estimate the pose and velocity of a ground vehicle in the navigation frame.

## 

Scott's videos
tutorial on how to implement an IMU using a conventional accelerometer, gyroscope, and magnetometer.
[video](https://www.youtube.com/watch?v=T9jXoG0QYIA&t=573s)

[video](https://www.youtube.com/watch?v=6M6wSLD-8M8&t=687s)

Qualitative comparison between GNSS and INS
|                       	| GPS(GNSS) 	| IMS(INS) 	|
|-----------------------	|--------------	|-------	|
| acquisition frequency 	|  low         	|    high 	|
| location              	|       values referenced to some absolute position     	|   subject to drift - accumulated error over time    	|
| accuracy short term   	|  low         	|      high 	|

# Methodology

## Sensor Fusion Architecture

```sequence {theme="hand"}
Title: Extended Kalman Filter - functioning on a single axis
Note over EKF: Prediction
Note over IMU: high rate
Note over GPS: low rate
IMU->EKF: accelaration
Note over EKF: Update
GPS->EKF: position
Note left of EKF: position &\n velocity 

```

## Calibration

### IMU Calibration


### GPS Calibration




By default the library returns 3-tuple of X, Y, Z axis values for either acceleration, gyroscope and magnetometer ie compass. Default units are `m/s^2`, `rad/s`, `uT` and `°C`. It is possible to also get acceleration values in `g` and gyro values `deg/s`

# Preliminary Results
Before integrating the various components on the sensor system, individual tests were performed on each module to ensure understand and tune each proper functionality.


## Roll Yaw and Pitch axes from IMU Sensor through a RVIZ ROS vizualization
This simulation was based on the one performed by the Oregon State University found in this [video](https://www.youtube.com/watch?v=a-mfCeykmYw).



## GPS coordenates mapping on 

# Conclusions


## Credits
* https://github.com/UASLab/OpenFlight/blob/master/FlightCode/navigation/EKF_15state_quat.c
* https://github.com/FlyTheThings/uNavINS