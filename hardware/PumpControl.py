import RPi.GPIO as GPIO
import time
import threading



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
        

    def runPumpAsync(self, timeWait):
        self.thread = PumpThread(self, timeWait)
        self.thread.start()

    def join(self):
        if self.thread is not None :
            self.thread.join()

class PumpThread (threading.Thread):
    def __init__(self, parent, timeWait):
        threading.Thread.__init__(self)
        self.parent = parent
        self.timeWait = timeWait
        
    def run(self):
        parent.runPump(self.timeWait)