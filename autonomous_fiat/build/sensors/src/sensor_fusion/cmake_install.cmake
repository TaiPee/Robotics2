# Install script for directory: /home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/sensors/src/sensor_fusion

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensor_fusion/msg" TYPE FILE FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/sensors/src/sensor_fusion/msg/states.msg")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensor_fusion/cmake" TYPE FILE FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusion-msg-paths.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/devel/include/sensor_fusion")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/devel/share/roseus/ros/sensor_fusion")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/devel/share/common-lisp/ros/sensor_fusion")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/devel/share/gennodejs/ros/sensor_fusion")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/devel/lib/python2.7/dist-packages/sensor_fusion")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/devel/lib/python2.7/dist-packages/sensor_fusion")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusion.pc")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensor_fusion/cmake" TYPE FILE FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusion-msg-extras.cmake")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensor_fusion/cmake" TYPE FILE FILES
    "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusionConfig.cmake"
    "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusionConfig-version.cmake"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sensor_fusion" TYPE FILE FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/src/sensors/src/sensor_fusion/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensor_fusion" TYPE PROGRAM FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusion_main.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensor_fusion" TYPE PROGRAM FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusion_handle.py")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sensor_fusion" TYPE PROGRAM FILES "/home/david/Documents/Tecnico/SecondQuarter/Robotics/Lab2/Robotics2/autonomous_fiat/build/sensors/src/sensor_fusion/catkin_generated/installspace/sensor_fusion_pipeline.py")
endif()

