import RPi.GPIO as GPIO
import PumpControl
import time

GPIO.setmode(GPIO.BCM)

pumpYellow = PumpControl.PumpControl(25)
pumpGreen = PumpControl.PumpControl(24)
pumpBlue = PumpControl.PumpControl(23)


pumpYellow.runPumpAsync(5)
pumpBlue.runPumpAsync(1)
pumpGreen.runPumpAsync(3)


pumpYellow.join()
pumpBlue.join()
pumpGreen.join()


GPIO.cleanup()




