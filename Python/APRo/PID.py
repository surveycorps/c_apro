class PID:
    setpoint 
    dt = -1
    def __init__(self, setpoint, p=2, i=0, d=1):
        self.setpoint = setpoint
        self.kp = p
        self.kd = d
        self.ki = i
        self.previous_error = 0
        self.integral = 0

    def update(self, measured, dt):
        # Used a pre-determined delta time if it was set
        if (self.dt > 0):
            dt = self.dt

        error = (self.setpoint - measured)
        self.integral = self.ki * (self.integral + (error * dt))
        derivative = self.kd * ((error - self.previous_error)/dt)
        output = self.kp * error + self.integral + derivative
        previous_error = error
        return output
        
         
