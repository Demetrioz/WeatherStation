import machine
from utime import ticks_ms, ticks_diff, sleep
from math import pi


CM_TO_MI_FACTOR = 44.704
MEASURE_TIME_S = 5
DEBOUNCE_DURATION_MS = 20
ANEMOMETER_RADIUS_CM = 9
ANEMOMETER_FACTOR = 1.18 # https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/5

class Anemometer():
    # TODO:
    # Take regular 5 second readings and store them for an average wind speed
    # Take the highest value for the gust
    # measure_wind_speed should find / return the average & max, then clear the data
    
    def __init__(self):
        self.circumference_cm = (2 * pi) * ANEMOMETER_RADIUS_CM
        self.spin_triggers = 0
        self.debounce_timer = ticks_ms()
        self.anemometer = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
        self.anemometer.irq(trigger=machine.Pin.IRQ_RISING, handler=self.spin_handler)
        
        
    # triggers 4 times per rotation
    def spin_handler(self, pin):
        now = ticks_ms()
        if ticks_diff(now, self.debounce_timer) > DEBOUNCE_DURATION_MS:
            self.debounce_timer = now
            self.spin_triggers = self.spin_triggers + 1


    def calculate_wind_speed(self, time_s):
        rotations = self.spin_triggers / 4
        distance_cm = self.circumference_cm * rotations
        speed_cm_s = distance_cm / time_s
        return speed_cm_s * ANEMOMETER_FACTOR
    
    
    def calculate_wind_speed_mph(self, time_s):
        rotations = self.spin_triggers / 4
        distance_cm = self.circumference_cm * rotations
        speed_cm_s = distance_cm / time_s
        speed_mi_h = speed_cm_s / CM_TO_MI_FACTOR
        return speed_mi_h * ANEMOMETER_FACTOR
    
    
    def measure_wind_speed(self):
        self.spin_triggers = 0
        sleep(MEASURE_TIME_S)
        return self.calculate_wind_speed(MEASURE_TIME_S);