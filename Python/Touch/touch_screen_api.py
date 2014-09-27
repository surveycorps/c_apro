from Adafruit_I2C import Adafruit_I2C
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

class touch:
    def __init__(self,data):
	# Hardcoded offset to diffrentiate between each touch data
        offset = [1, 8, 15, 22]
        self.data = data
	# Integer representing how many individual touches were detected
	self.touches = data[0] & 0x7 
	# An array of boolean values representing if an individual touch was detected
	self.touches_array = [x < self.touches for x in range(len(offset))]

        ## Sort out data
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


I2C_IQS550_ADDR = 0x74
REG_XY_DATA = 0x01
# Although 5 touches are available in total (36 Bytes) the max the smbus-python library can read at a time is 32 (Bytes) thus this library is restricted to 4 touches (32 Bytes)
XY_DATA_SIZE = 32 

DATA_RDY_PIN = "P9_12" # High when there is available XY Data to be read
HARD_RST_PIN = "P9_17" # Normally Low, does not need to be used in most cirumstances
touch_i2c = Adafruit_I2C(I2C_IQS550_ADDR);

GPIO.setup(DATA_RDY_PIN, GPIO.IN);
GPIO.setup(HARD_RST_PIN, GPIO.OUT);

while (GPIO.input(DATA_RDY_PIN) == 0):
    continue

while True:
    sleep(0.01)
    if GPIO.input(DATA_RDY_PIN):
        data = touch_i2c.readList(REG_XY_DATA, XY_DATA_SIZE)
	if (data < 0):
	    continue
        d = touch(data)
	if (data == d):
            continue
        print("(%.1f, %.1f) Touches: %d" % (d.x_pos[0], d.y_pos[0], d.touches))	
	print(data)
	print("\n")
