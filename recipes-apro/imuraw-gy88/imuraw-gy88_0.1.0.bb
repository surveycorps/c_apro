DESCRIPTION = "ROS Node which publishes raw imu data (linear acceleration/angular velocity) to "imu/data_raw" topic as sensor_msgs.IMU and raw magnometer data (magnetic field) to "imu/mag" topic."
SECTION = "devel"
LICENSE = "BSD"
LIC_FILES_CHKSUM ="file://package.xml;;beginline=8;endline=8;md5=01c2bc31767ccb3a68e12f02612b2a97"

DEPENDS = "catkin rospy std-msgs sensor-msgs geometry-msgs"

SRC_URI = "git://github.com/surveycorps/imuraw_gy88.git"
SRC_URI[md5sum] = "a001a2af7d75092f3dc851bde57d7ec8"

SRCREV = "0ff0ea0fa7efcdcbbb23cdfa30d5d6ea28510d08"

S = "${WORKDIR}/git"

inherit catkin
