import Adafruit_BBIO.GPIO as GPIO
from time import sleep
import time

start = 0
stop = 0
CONST_TOINCH = (13397.2441)/2 

# Set up hardware pins
TRIG_PIN = "P9_13"
ECHO_PIN = "P9_14"
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 

GPIO.output(TRIG_PIN, GPIO.LOW)

# Allow GPIO to setup for some time
sleep(0.1)

skip_section = False

while True:
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)

        start = time.time()
        start_wait = start 
        while GPIO.input(ECHO_PIN) == 0:
              start = time.time()
              if((start - start_wait) > 1):
                skip_section = True
                break
        while GPIO.input(ECHO_PIN) == 1:
              stop = time.time()
              if ((stop-start) > 1):
                skip_section = True
                break

        if (skip_section):
              continue

        elapsed = stop - start
        distance = (elapsed*CONST_TOINCH)
        print("Distance (in): %f" % distance)
