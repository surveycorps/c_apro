#!/usr/bin/env python
from Adafruit_I2C import Adafruit_I2C
from operator import add, div

import time


class IMU : 

    #TODO: Port all array operation (currently using map) to numpy

    MPU6050_I2C_ADDRESS = 0x68
    HMC5883L_I2C_ADDRESS = 0x1E 
    #TODO: Handle magnometer gain settings, see Adafruit implementation

    RAW2ACCEL = 16384 # Conversion factor from raw byte value to g's 
    RAW2GYRO = 131 # Conversion factor from raw byte value to rad/s 
    RAW2MAG = 1

    """
    Define Register values
    """

    REG_MAG_CONT_MODE = 0x02
    REG_IMU_RESET = 0x6B 

    REG_ACCEL_X_HI = 0x3b
    REG_ACCEL_X_LOW = 0x3c
    REG_ACCEL_Y_HI = 0x3d
    REG_ACCEL_Y_LOW = 0x3e
    REG_ACCEL_Y_HI = 0x3f
    REG_ACCEL_Y_LOW = 0x40

    REG_GYRO_X_HI = 0x43
    REG_GYRO_X_LOW = 0x44
    REG_GYRO_Y_HI = 0x45
    REG_GYRO_Y_LOW = 0x46
    REG_GYRO_Z_HI = 0x47
    REG_GYRO_Z_LOW = 0x48
    
    REG_MAG_X_HI = 0x03
    REG_MAG_X_LOW = 0x04
    REG_MAG_Y_HI = 0x07
    REG_MAG_Y_LOW = 0x08
    REG_MAG_Z_HI = 0x05
    REG_MAG_Z_LOW = 0x06
    # Not yet implemented 
    #removeGravity = False
    #lp_g = [0,0,0]

    def __init__(self, enableMag = False):
        self.accel_bias = [0, 0, 0]
        self.gyro_bias = [0, 0, 0]

        self.i2c_imu = Adafruit_I2C(self.MPU6050_I2C_ADDRESS)
        # Power reset, needed to wake up the MPU6050
        self.i2c_imu.write8(self.REG_IMU_RESET, 0)
        
        if (enableMag):
            self.i2c_mag = Adafruit_I2C(self.HMC5883L_I2C_ADDRESS)
            # Set the Magnometer to continous read mode
            self.i2c_mag.write8(self.REG_MAG_CONT_MODE, 0)

    @staticmethod
    def _twos_comp(val, bits):
        if((val&(1<<(bits-1))) != 0 ):
            val = val - (1<<bits)
        return val

    def _reg2raw(self, i2c, high, low):
        b_high = i2c.readU8(high) & 0xFF
        b_low = i2c.readU8(low) & 0xFF
        return self._twos_comp((b_high << 8 | b_low), 16)

    # Get bias as the simple average of values in a non-inertial frame 
    def get_bias(self, sensor, counts=100, duration=None):

        bias = [0,0,0]

        if (duration is None):
            for i in range(0, counts):
                bias = map(add, bias, sensor()) 
                bias[:] = [val / counts for val in bias]
        else:
            start = time.time()
            count = 0
            while (start - time.time() < duration):
                count += 1
                bias = map(add, bias, self.sensor())
                bias[:] = [val / count for val in bias]
    
        return bias


    def get_accel_bias(self, counts=100, duration=None):
        self.accel_bias = get_bias(self, self.accel, counts, duration) 

    def get_gyro_bias(self, counts=100, duration=None):
        self.gyro_bias = get_bias(self, self.gyro, counts, duration) 

    def accel(self):
        a = [self.accel_x(), self.accel_y(), self.accel_z()]
        return a
    
    def gyro(self):
        g = [self.gyro_x(), self.gyro_y(), self.gyro_z()]
        return g

    def accel_x(self):
        raw = self._reg2raw(self.i2c_imu, self.REG_ACCEL_X_HI, self.REG_ACCEL_X_LOW)
        return float(raw)/self.RAW2ACCEL 

    def accel_y(self):
        raw = self._reg2raw(self.i2c_imu, self.REG_ACCEL_Y_HI, self.REG_ACCEL_Y_LOW)
        return float(raw)/self.RAW2ACCEL 

    def accel_z(self):
        raw = self._reg2raw(self.i2c_imu, self.REG_ACCEL_Z_HI, self.REG_ACCEL_Z_LOW)
        return float(raw)/self.RAW2ACCEL 

    def gyro_x(self):
        raw = self._reg2raw(self.i2c_imu, self.REG_GYRO_X_HI, self.REG_GYRO_X_LOW)
        return float(raw)/self.RAW2GYRO

    def gyro_y(self):
        raw = self._reg2raw(self.i2c_imu, self.REG_GYRO_Y_HI, self.REG_GYRO_Y_LOW)
        return float(raw)/self.RAW2GYRO

    def gyro_z(self):
        raw = self._reg2raw(self.i2c_imu, self.REG_GYRO_Z_HI, self.REG_GYRO_Z_LOW)
        return float(raw)/self.RAW2GYRO

    def mag_x(self):
        raw = self._reg2raw(self.i2c_mag, self.REG_MAG_X_HI, self.REG_MAG_X_LOW)
        return float(raw)/self.RAW2MAG

    def mag_y(self):
        raw = self._reg2raw(self.i2c_mag, self.REG_MAG_Y_HI, self.REG_MAG_Y_LOW)
        return float(raw)/self.RAW2MAG

    def mag_z(self):
        raw = self._reg2raw(self.i2c_mag, self.REG_MAG_Z_HI, self.REG_MAG_Z_LOW)
        return float(raw)/self.RAW2MAG


