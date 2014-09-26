from Adafruit_I2C import Adafruit_I2C
import Adafruit_BBIO.GPIO as GPIO

I2C_IQS550_ADDR = 0x74
REG_XY_DATA = 0x01
XY_DATA_SIZE = 36

DATA_RDY_PIN = 'P9_16' # High when there is available XY Data to be read
HARD_RST_PIN = 'P9_17' # Normally Low

touch_i2c = Adafruit_I2C(I2C_IQS550_ADDR);
GPIO.setup(DATA_RDY_PIN, GPIO.IN);
# GPIO.setup(DATA_RDY_PIN, GPIO.OUT);

while True:
    if (GPIO.input(DATA_RDY_PIN)):
       data = readList(REG_XY_DATA, XY_DATA_SIZE)
       print(data)

class touch:
    def __init__(self,data):
        offset = [2, 9, 16, 23, 30]
        self.data = data
        # Sort out data
        self.tag = [data[i] for i in offset]
        x_pos_hi = [data[i+1] for i in offset]
        x_pos_lo = [data[i+2] for i in offset]
        y_pos_hi = [data[i+3] for i in offset]
        y_pos_lo = [data[i+4] for i in offset]
        strength_hi = [data[i+5] for i in offset]
        strength_lo = [data[i+6] for i in offset]

        self.x_pos = [(hi<<8 | lo)for hi in x_pos_hi for lo in x_pos_lo] 
        self.y_pos = [(hi<<8 | lo)for hi in y_pos_hi for lo in y_pos_lo] 
        self.strength = [(hi<<8 | lo)for hi in y_pos_hi for lo in y_pos_lo] 



