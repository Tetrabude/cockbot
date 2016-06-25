try:
	import RPi.GPIO as GPIO
	from hardware.PumpControlPi import PumpControlPi as PumpControl
	print("Pi loaded")
except ImportError:
	from hardware.PumpControlMock import PumpControlMock as PumpControl
	print("Mock loaded")

class CleaningController:
	def __init__(self):
		print('test')
		
	def start(self, pump, duration):
		print("Pump with ID: " + pump.name)
		
			#for pump in pumps:
		pumpDevice = PumpControl(pump.gpioId)
		pumpDevice.runPumpAsync(duration)
