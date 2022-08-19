import machine
import utime

CONVERSION_FACTOR = 5 / 65535 # 5v / highest reading
VOLT_ANGLES = {
    3.2: 0,
    1.2: 45,
    0.2: 90,
    0.4: 135,
    0.6: 180,
    2.0: 225,
    5.0: 270,
    4.5: 315,
}
ANGLE_DIRECTIONS = {
    0: "N",
    45: "NE",
    90: "E",
    135: "SE",
    180: "S",
    225: "SW",
    270: "W",
    315: "NW"
}

class WindVane():
    def __init__(self):
        self.wind_vane = machine.ADC(26)


    def measure_wind_direction(self):
        voltage = round(self.wind_vane.read_u16() * CONVERSION_FACTOR, 1)
        print(f"Voltage: {voltage}")
        angle = VOLT_ANGLES[voltage]
        print(f"Angle: {angle}")
        if angle is not None:
            direction = ANGLE_DIRECTIONS[angle]
            print(f"Direction: {direction}")
            return direction

#CONVERSION_FACTOR = 5 / (65535)

#wind_vane = machine.ADC(26)

#while True:
#    voltage = wind_vane.read_u16() * CONVERSION_FACTOR
#    print(voltage)
#    utime.sleep(2)


#3.23 = 0
#1.19 = 45
#0.19 / 0.20 = 90
#0.38 / 0.39 = 135
#0.62 = 180
#2.00 = 225
#5.0 = 270
#4.5 = 315