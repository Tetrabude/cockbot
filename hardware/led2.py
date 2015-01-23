import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)
while GPIO.input(24)==False:
    GPIO.output(25, 1)
    time.sleep(2)
    GPIO.output(25, 0)
    time.sleep(2)
GPIO.cleanup()

