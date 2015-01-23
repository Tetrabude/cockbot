import Rpi.GPIO as GPIO
import PumpControl

GPIO.setmode(GPIO.BCM)

pumpA = PumpControl(25)

pumpA.runPump(5)

GPIO.cleanup()