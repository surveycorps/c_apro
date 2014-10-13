#!/usr/bin/env python
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

import rospy
from std_msgs.msg import Float32

class MotorEnc():
    
    PIN_LEFT_ENC = "p9_18"
    PIN_RIGHT_ENC = "p9_19"
    PIN_SHELL_ENC = "p9_20"
    
    PIN_LEFT_DIR = "p9_21"
    PIN_RIGHT_DIR = "p9_22"
    PIN_SHELL_DIR = "p9_23"

    MOTOR_LEFT = "motor_left"
    MOTOR_RIGHT = "motor_right"
    MOTOR_SHELL = "motor_shell"

    ## Conversion Factors
    #TODO: Update with correct conversion factor
    # Convert raw values from ADC to Revolutions per Second 
    RAW2REV = 1
    # Convert Revolutions per Second to Meters per Second
    VEL2DIST = 1 
    
    def __init__(self):
        ## Set up ROS Node
        rospy.init_node("motor_enc")
        self.nodename = rospy.get_name()
        self.rate = rospy.Rate(10)
        
        # Publish velocity of each wheel 
        self.pub_w_l = rospy.Publisher('enc/lwheel', Float32)
        self.pub_w_r = rospy.Publisher('enc/rwheel', Float32)
        # Publish distance traveled by each wheel
        self.pub_dist_l = rospy.Publisher('data/ldist', Float32)
        self.pub_dist_r = rospy.Publisher('data/rdist', Float32)

        # A map from motor names to their pin number on the BBB
        self.pin_map = {self.MOTOR_LEFT:self.PIN_LEFT_ENC,
                self.MOTOR_RIGHT:self.PIN_RIGHT_ENC,
                self.MOTOR_SHELL:self.PIN_SHELL_ENC}

        # Map from motor names to their direction pin number
        self.dir_map = {self.MOTOR_LEFT:self.PIN_LEFT_DIR,
                self.MOTOR_RIGHT:self.PIN_RIGHT_DIR,
                self.MOTOR_SHELL:self.PIN_SHELL_DIR}

        ## Set up IO
        ADC.setup()

        ## Initialize important values
        self.w_l = 0 # Left wheel angular velocity
        self.w_r = 0 # Right wheel angular velocity

        self.dist_l = 0 # 
        self.dist_r = 0 
        
        # Time management
        self.then = rospy.Time.now() 
    
    def spin(self):
        while not rospy.is_shutdown():
            self.update()
            r.sleep()

    def getAngularVelocity(self, m):
        if m in self.pin_map:
            pin = self.pin_map[m]
        else:
            return None #TODO: Handle Gracefully

        # There's currently a bug in the Adafruit library where the ADC pin must
        # be read twice to get the latest value. 
        ADC.read(pin)
        raw_value = ADC.read(pin)
        value = self.RAW2REV * raw_value

    def update(self):
        self.now = rospy.Time.now()

        self.w_l = self.getAngularVelocity(self.MOTOR_LEFT)
        self.w_r = self.getAngularVelocity(self.MOTOR_RIGHT)

        # Convert from angular velocity to linear velocity
        vel_l = VEL2DIST * w_l
        vel_r = VEL2DIST * w_r

        dt = self.now - self.then
        self.dist_l = self.dist_l + vel_l*dt
        self.dist_r = self.dist_r + vel_r*dt

        ## Publish Data
        # Angular Velocity Left
        p_w_l = Float32()
        p_w_l.data = self.w_l
        pub_w_l.publish(p_w_l)
        # Angular Velocity Right
        p_w_r = Float32()
        p_w_r.data = self.w_r
        pub_w_r.publish(p_w_r)
        # Distance Traveled Left
        p_dist_l = Float32()
        p_dist_l.data = self.dist_l
        pub_dist_l.publish(p_dist_l)
        # Distance Traveled Right
        p_dist_r = Float32()
        p_dist_r.data = self.dist_r
        pub_dist_r.publish(p_dist_r)

        # Update time
        self.then = self.now

         





