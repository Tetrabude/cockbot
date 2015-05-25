from django.apps import AppConfig
from barkeeper.models import Pump

try:
    import RPi.GPIO as GPIO
    from hardware.PumpControlPi import PumpControlPi as PumpControl
    print("Pi loaded")
except ImportError:
    from hardware.PumpControlMock import PumpControlMock as PumpControl
    print("Mock loaded")

class BarkeeperConfig(AppConfig):
    name = 'barkeeper'
    
        
    def ready(self):
        print("Ich bin voll ready!")
        self.resetAllPumps()
            
    def resetAllPumps(self):
        print("Resetting pumps:")
        for pump in Pump.objects.all():
            print("Pump " + pump.name + " on GPIO " + str(pump.gpioId))
            tmp = PumpControl(pump.gpioId)
            
            