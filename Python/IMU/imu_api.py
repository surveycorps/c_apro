from Adafruit_I2C import Adafruit_I2C

class IMU : 
        I2C_ADDRESS = 0x68
        REG_I2C_RESET = 0x6B 
        RAW2ACCEL = 16384 
        RAW2GYRO = 131

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

        def __init__(self):
                self.i2c = Adafruit_I2C(self.I2C_ADDRESS)
                self.i2c.write8(self.REG_I2C_RESET, 0)

        @staticmethod
        def _twos_comp(val, bits):
                if((val&(1<<(bits-1))) != 0 ):
                        val = val - (1<<bits)
                return val

        def _reg2raw(self, high, low):
                b_high = self.i2c.readU8(high) & 0xFF
                b_low = self.i2c.readU8(low) & 0xFF
                return self._twos_comp((b_high << 8 | b_low), 16)


        def getAccelX(self):
                raw = self._reg2raw(self.REG_ACCEL_X_HI, self.REG_ACCEL_X_LOW)
                return float(raw)/self.RAW2ACCEL 

        def getAccelY(self):
                raw = self._reg2raw(self.REG_ACCEL_Y_HI, self.REG_ACCEL_Y_LOW)
                return float(raw)/self.RAW2ACCEL 

        def getAccelZ(self):
                raw = self._reg2raw(self.REG_ACCEL_Z_HI, self.REG_ACCEL_Z_LOW)
                return float(raw)/self.RAW2ACCEL 

        def getGyroX(self):
                raw = self._reg2raw(self.REG_GYRO_X_HI, self.REG_GYRO_X_LOW)
                return float(raw)/self.RAW2GYRO
        def getGyroY(self):
                raw = self._reg2raw(self.REG_GYRO_Y_HI, self.REG_GYRO_Y_LOW)
                return float(raw)/self.RAW2GYRO

        def getGyroZ(self):
                raw = self._reg2raw(self.REG_GYRO_Z_HI, self.REG_GYRO_Z_LOW)
                return float(raw)/self.RAW2GYRO