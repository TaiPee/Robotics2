# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include".split(';') if "${prefix}/include;/usr/include" != "" else []
PROJECT_CATKIN_DEPENDS = "dynamic_reconfigure;geometry_msgs;message_filters;nodelet;pluginlib;roscpp;sensor_msgs;tf2_geometry_msgs;tf2_ros".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-limu_filter;-limu_filter_nodelet;/usr/lib/aarch64-linux-gnu/libboost_system.so.1.71.0;/usr/lib/aarch64-linux-gnu/libboost_thread.so.1.71.0".split(';') if "-limu_filter;-limu_filter_nodelet;/usr/lib/aarch64-linux-gnu/libboost_system.so.1.71.0;/usr/lib/aarch64-linux-gnu/libboost_thread.so.1.71.0" != "" else []
PROJECT_NAME = "imu_filter_madgwick"
PROJECT_SPACE_DIR = "/home/taipee/Documents/Robotics2/autonomous_fiat/src/sensors/install"
PROJECT_VERSION = "1.2.5"
