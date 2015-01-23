import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
while True:
    if GPIO.input(24)==True:
        print("Ja!")
    else:
        print("Nein...")
    time.sleep(1)
GPIO.cleanup()

