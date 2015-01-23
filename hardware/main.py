#import RPi.GPIO as GPIO
#from PumpControlPi import PumpControlPi as PumpControl
from PumpControlMock import PumpControlMock as PumpControl
import time

#GPIO.setmode(GPIO.BCM)

pumpYellow = PumpControl(25)
pumpGreen = PumpControl(24)
pumpBlue = PumpControl(23)


pumpYellow.runPumpAsync(5)
pumpBlue.runPumpAsync(1)
pumpGreen.runPumpAsync(3)


pumpYellow.join()
pumpBlue.join()
pumpGreen.join()


#GPIO.cleanup()




