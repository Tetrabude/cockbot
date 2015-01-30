from abc import ABCMeta, abstractmethod

import threading



class PumpControl:
    """Starts pump for time range"""
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def __init__(self, gpioId):
        self.gpioId = gpioId
        self.thread = None
        
    description = "Connects gpio slot to pump and activates pump for time range"
    author = "smeky, poschi"

    @abstractmethod
    def runPump(self, timeWait): pass
        

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
        self.parent.runPump(self.timeWait)
