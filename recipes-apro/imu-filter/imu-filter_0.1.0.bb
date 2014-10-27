DESCRIPTION = "Filter which fuses angular velocities, accelerations, and (optionally) magnetic readings from a generic IMU device into an orientation. Based on code by Sebastian Madgwick, http://www.x-io.co.uk/node/8#open_source_ahrs_and_imu_algorithms."
SECTION = "devel"
LICENSE = "GPL"
LIC_FILES_CHKSUM ="file://package.xml;;beginline=7;endline=7;md5=162b49cfbae9eadf37c9b89b2d2ac6be"

DEPENDS = "roscpp catkin rospy std-msgs sensor-msgs geometry-msgs tf nodelet message-filters dynamic-reconfigure"

SRC_URI = "git://ithub.com/surveycorps/imu_tools.git;branch=hydro-filter-only"
SRC_URI[md5sum] = "bfc69a2d0b5bc36d9cb7617fdc557f05"

SRCREV = "e3b52b1ac2b2c4a8e1c39e30a8be3e2201d13b68"

S = "${WORKDIR}/imu_filter"

inherit catkin
