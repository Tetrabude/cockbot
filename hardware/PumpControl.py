import RPi.GPIO as GPIO
import time

class PumpControl:
    """Starts pump for time range"""
    
    def __init__(self, gpioId):
        self.gpioId = gpioId
        GPIO.setup(gpioId, GPIO.OUT)
        
    description = "Connects gpio slot to pump and activates pump for time range"
    author = "smeky, poschi"
    
    def runPump(self, time):
        GPIO.output(gpioId, 1)
        time.sleep(time)
        GPIO.output(gpioId, 0)
        