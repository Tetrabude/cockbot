from abc import ABCMeta, abstractmethod
from PumpControl import PumpControl

import time

class PumpControlMock(PumpControl):
    """Starts simulation for time range"""
    
    def __init__(self, gpioId):
        super(PumpControlMock,self).__init__(gpioId)
            
    def runPump(self, timeWait):
        print "start: " + str(self.gpioId)
        time.sleep(timeWait)
        print "stop: " + str(self.gpioId)
        return True