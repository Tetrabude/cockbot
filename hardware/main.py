import RPi.GPIO as GPIO
import PumpControl

from multiprocessing import Pool
pool = Pool()

GPIO.setmode(GPIO.BCM)

pumpYellow = PumpControl.PumpControl(25)
pumpGreen = PumpControl.PumpControl(24)
pumpBlue = PumpControl.PumpControl(23)

pool.apply_async(pumpYellow.runPump, [5])
pool.apply_async(pumpBlue.runPump, [1])
pool.apply_async(pumpGreen.runPump, [3])

GPIO.cleanup()




