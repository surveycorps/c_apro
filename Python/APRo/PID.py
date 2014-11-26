class PID:
    dt = -1
    def __init__(self, setpoint, p=2, i=0, d=1):
        self.setpoint = setpoint
        self.kp = p
        self.kd = d
        self.ki = i
        self.previous_error = 0
        self.integral = 0 
        self.limits = False
        self.lower = None
        self.upper = None

    def update(self, measured, dt):
        # Used a pre-determined delta time if it was set
        if (self.dt > 0):
            dt = self.dt
        dt = float(dt)

        error = (self.setpoint - measured)
        self.integral = self.ki * (self.integral + (error * dt))
        derivative = self.kd * ((error - self.previous_error)/dt)
        output = self.kp * error + self.integral + derivative

        if (limits): 
            output = _obey_limit(output)
            error = _obey_limit(error)

        self.previous_error = error

        return output
        
    def set_limits(self, l_min, l_max):
        self.limits = True
        self.lower = l_min
        self.upper = l_max

    def _obey_limit(value):
        if (value > self.upper):
            value = self.upper

        elif (value < self.lower):
            value = self.lower

        return value
