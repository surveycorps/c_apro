import Adafruit_BBIO.PWM as PWM

class Motor:
    PIN_M_LEFT = "P9_14"
    PIN_M_RIGHT = "P9_14"
    PIN_M_LEFT_DIR = "P9_14"
    PIN_M_RIGT_DIR = "P9_14"
    BASE_FREQ = 40000

    def __init__(self):
        PWM.start(PIN_M_LEFT, 0, BASE_FREQ) 
        PWM.start(PIN_M_RIGHT, 0, BASE_FREQ)

    def __del__(self):
        PWM.stop(PIN_M_LEFT)
        PWM.stop(PIN_M_RIGHT)

    def turn(self, theta, motor="both"):
        #TODO: Implement method
        pass
    
    def left(self, vel):
        if vel < -100 or vel > 100:
            raise ValueError("Invalid motor speed range. Please use values within the range [-100 100]")
        PWM.set_duty_cycle(IN_M_LEFT, vel)

    def right(self, vel):
        if vel < -100 or vel > 100:
            raise ValueError("Invalid motor speed range. Please use values within the range [-100 100]")
        PWM.set_duty_cycle(IN_M_LEFT, vel)

