import RPi.GPIO as GPIO
import PumpControl

GPIO.setmode(GPIO.BCM)

pumpA = PumpControl.PumpControl(25)

pumpA.runPump(5)

GPIO.cleanup()
