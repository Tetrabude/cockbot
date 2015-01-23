import RPi.GPIO as GPIO
import PumpControl

GPIO.setmode(GPIO.BCM)

pumpYellow = PumpControl.PumpControl(25)
pumpGreen = PumpControl.PumpControl(24)
pumpBlue = PumpControl.PumpControl(23)

pumpYellow.runPump(5)
pumpBlue.runPump(1)
pumpGreen.runPump(3)

GPIO.cleanup()
