DESCRIPTION = "ROS Node which publishes raw imu data (linear acceleration/angular velocity) to "imu/data_raw" topic as sensor_msgs.IMU and raw magnometer data (magnetic field) to "imu/mag" topic."
SECTION = "devel"
LICENSE = "MIT"
LIC_FILES_CHKSUM ="file://package.xml;;beginline=7;endline=7;md5=05c8b019cf5b0834bc5e547a14f26ca3"

DEPENDS = "catkin rospy std-msgs sensor-msgs geometry-msgs"

SRC_URI = "https://github.com/surveycorps/imuraw_gy88"
SRC_URI[md5sum] = "a001a2af7d75092f3dc851bde57d7ec8"
SRC_URI[sha256sum] = "a5fbcd0167a4782eae1fb1525251e6bad0d310240c73609beb98bcd2a0bfcfbc"

S = "${WORKDIR}/${ROS_SP}"

inherit catkin
