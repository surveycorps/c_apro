DESCRIPTION = "Filter which fuses angular velocities, accelerations, and (optionally) magnetic readings from a generic IMU device into an orientation. Based on code by Sebastian Madgwick, http://www.x-io.co.uk/node/8#open_source_ahrs_and_imu_algorithms."
SECTION = "devel"
LICENSE = "GPL"
LIC_FILES_CHKSUM ="file://imu_filter_madgwick/package.xml;;beginline=7;endline=7;md5=05c8b019cf5b0834bc5e547a14f26ca3"

DEPENDS = "roscpp catkin rospy std-msgs sensor-msgs geometry-msgs tf nodelet message-filters dynamic-reconfigure"

SRC_URI = "https://github.com/ccny-ros-pkg/imu_tools.git;branch=hydro"
SRC_URI[md5sum] = "a001a2af7d75092f3dc851bde57d7ec8"
SRC_URI[sha256sum] = "a5fbcd0167a4782eae1fb1525251e6bad0d310240c73609beb98bcd2a0bfcfbc"

S = "${WORKDIR}/${ROS_SP}"

inherit catkin
