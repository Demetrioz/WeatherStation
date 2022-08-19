import network
import secrets

from lib.weather_station.thp_sensor import ThpSensor
from lib.weather_station.ground_sensor import GroundSensor
from lib.weather_station.anemometer import Anemometer
from lib.weather_station.wind_vane import WindVane
from lib.weather_station.rain_guage import RainGuage

class WeatherStation():
    def __init__(self) -> None:
        self.wlan = None
        self.thp_sensor = ThpSensor()
        self.ground_sensor = GroundSensor()
        self.anemometer = Anemometer()
        self.wind_vane = WindVane()
        self.rain_guage = RainGuage()


    def initialize_wireless(self):
        print("Starting wireless")
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        print(f"SSID: {secrets.SSID}")
        while not self.wlan.isconnected():
            self.wlan.connect(secrets.SSID, secrets.PASSWORD)
            print(f"Connected: {self.wlan.isconnected()}")
            
    
    def read_thp_sensor(self):
        print("Temperature: %0.1f F" % self.thp_sensor.get_temperature_f())
        
        
    def read_ground_sensor(self):
        print("OneWire Temperature: %0.1f F" % self.ground_sensor.get_temperature_f())
     
     
    def determine_wind_speed(self):
        print("Wind speed: %0.1f cm/s" % self.anemometer.measure_wind_speed())
        
 
    def determine_wind_direction(self):
        print(f"Wind direction: {self.wind_vane.measure_wind_direction()}")
     
 
    def read_rain_guage(self):
        print("Rain: %0.1f mm" % self.rain_guage.measure_rainfall())