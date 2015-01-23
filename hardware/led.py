import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
while True:
    GPIO.output(25, 1)
    time.sleep(2)
    GPIO.output(25, 0)
    time.sleep(2)
GPIO.cleanup()

