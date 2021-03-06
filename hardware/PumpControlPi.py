from abc import ABCMeta, abstractmethod
from hardware.PumpControl import PumpControl

import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    print("Problems with GPIO")
    
    

class PumpControlPi(PumpControl):
    """Starts pump for time range"""
    
    def __init__(self, gpioId):
        super(PumpControlPi,self).__init__(gpioId)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(gpioId, GPIO.OUT)
        GPIO.output(gpioId, 0)
            
    def runPump(self, timeWait):
        GPIO.output(self.gpioId, 1)
        time.sleep(timeWait)
        GPIO.output(self.gpioId, 0)
