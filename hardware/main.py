import RPi.GPIO as GPIO
import PumpControl

GPIO.setmode(GPIO.BCM)

pumpYellow = PumpControl.PumpControl(25)
pumpGreen = PumpControl.PumpControl(24)
pumpBlue = PumpControl.PumpControl(23)

pumpGreen.runPump(1)

pumpYellow.runPumpAsync(5)
pumpBlue.runPumpAsync(1)
pumpGreen.runPumpAsync(3)

pumpYellow.runPump(1)

GPIO.cleanup()



