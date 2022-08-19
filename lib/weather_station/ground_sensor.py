from machine import Pin
import onewire
import ds18x20

class GroundSensor():
    def __init__(self):
        self.ds_pin = Pin(2)
        self.ds_sensor = ds18x20.DS18X20(onewire.OneWire(self.ds_pin))
        self.rom = self.ds_sensor.scan()[0]
        print(f"ROM: {self.rom}")


    def get_temperature_f(self):
        self.ds_sensor.convert_temp()
        return self.ds_sensor.read_temp(self.rom) * 1.8 + 32
    
    
    def get_temperature_c(self):
        self.ds_sensor.convert_temp()
        return self.ds_sensor.read_temp(self.rom)