import machine
from utime import ticks_ms, ticks_diff, sleep

DEBOUNCE_DURATION_MS = 125
RAIN_MM_PER_TIP = 0.2794

class RainGuage():
    def __init__(self):
        self.tips = 0
        self.debounce_timer = ticks_ms()
        self.guage = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
        self.guage.irq(trigger=machine.Pin.IRQ_RISING, handler=self.tip_handler)
        
    
    def tip_handler(self, pin):
        now = ticks_ms()
        if ticks_diff(now, self.debounce_timer) > DEBOUNCE_DURATION_MS:
            self.debounce_timer = now
            self.tips = self.tips + 1
            
            
    def measure_rainfall(self):
        total_mm = self.tips * RAIN_MM_PER_TIP
        self.tips = 0
        return total_mm