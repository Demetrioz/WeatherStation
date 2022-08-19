from lib.weather_station.weather_station import WeatherStation
from utime import sleep

weather_station = WeatherStation()

weather_station.initialize_wireless()
weather_station.determine_wind_speed()
weather_station.determine_wind_direction()
weather_station.read_thp_sensor()
weather_station.read_ground_sensor()
weather_station.read_rain_guage()


while True:
    print("waiting...")
    sleep(2)