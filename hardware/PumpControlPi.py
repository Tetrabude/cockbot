from abc import ABCMeta, abstractmethod
from PumpControl import PumpControl

import time
import RPi.GPIO as GPIO

class PumpControlMock(PumpControl):
    """Starts pump for time range"""
    
    def __init__(self, gpioId):
        super(PumpControlMock,self).__init__(gpioId)
        GPIO.setup(gpioId, GPIO.OUT)
            
    def runPump(self, timeWait):
       GPIO.output(self.gpioId, 1)
       time.sleep(timeWait)
       GPIO.output(self.gpioId, 0)