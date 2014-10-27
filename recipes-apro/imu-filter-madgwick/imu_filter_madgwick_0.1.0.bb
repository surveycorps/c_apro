DESCRIPTION = "Filter which fuses angular velocities, accelerations, and (optionally) magnetic readings from a generic IMU device into an orientation. Based on code by Sebastian Madgwick, http://www.x-io.co.uk/node/8#open_source_ahrs_and_imu_algorithms."
HOMEPAGE = "http://ros.org/wiki/imu_filter_madgwick"
SECTION = "devel"
LICENSE = "GPL"
LIC_FILES_CHKSUM = "file://package.xml;beginline=7;endline=7;md5=162b49cfbae9eadf37c9b89b2d2ac6be"

DEPENDS = "catkin roscpp sensor-msgs geometry-msgs tf nodelet message-filters dynamic-reconfigure"

SRC_URI = "git://github.com/surveycorps/imu_tools.git;branch=hydro-filter-only;downloadfilename=${P}.tar.gz"
SRC_URI[md5sum] = ""
SRC_URI[sha256sum] = ""

S = "${WORKDIR}/-${PV}"

inherit catkin
