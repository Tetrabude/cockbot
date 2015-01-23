import RPi.GPIO as GPIO
import time

class PumpControl:
    """Starts pump for time range"""
    
    def __init__(self, gpioId):
        self.gpioId = gpioId
        GPIO.setup(gpioId, GPIO.OUT)
        
    description = "Connects gpio slot to pump and activates pump for time range"
    author = "smeky, poschi"
    
    def runPump(self, timeWait):
        GPIO.output(self.gpioId, 1)
        time.sleep(timeWait)
        GPIO.output(self.gpioId, 0)
        
