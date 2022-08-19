import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

class ThpSensor():
    def __init__(self):
        # Create sensor object, using the board's default I2C bus.
        self.i2c = busio.I2C(board.GP1, board.GP0) 
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c)
        # change this to match the location's pressure (hPa) at sea level
        self.bme280.sea_level_pressure = 1013.25
        
        #temp_f = self.bme280.temperature * 1.8 + 32
        #print("Temperature: %0.1f F" % temp_f)
        #print("Humidity: %0.1f %%" % self.bme280.relative_humidity)
        #print("Pressure: %0.1f hPa" % self.bme280.pressure)
        #print("Altitude = %0.2f meters" % self.bme280.altitude)
    
    
    def get_temperature_f(self):
        return self.bme280.temperature * 1.8 + 32
    
    
    def get_temperature_c(self):
        return self.bme280.temperature
    
    
    def get_humidity(self):
        return self.bme280.relative_humidity
    
    
    def get_pressure(self):
        return self.bme280.pressure
    
    
    def get_altitude(self):
        return self.bme280.altitude