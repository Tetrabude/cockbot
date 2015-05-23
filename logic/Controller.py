try:
	import RPi.GPIO as GPIO
	from hardware.PumpControlPi import PumpControlPi as PumpControl
	print("Pi loaded")
except ImportError:
	from hardware.PumpControlMock import PumpControlMock as PumpControl
	print("Mock loaded")

class Controller:
	def __init__(self, recipe):
		print("Cocktail: " + recipe.name)
		
		if not recipe.isPumpable():
			raise NameError("Nicht alle Zutaten sind an Pumpen angeschlossen")
		
		for ingredient in recipe.ingredient_set.all() :
			print(str(ingredient))
			
			pumps = ingredient.rawMaterial.pump_set.all()
			
			totalMlPerMin = 0.0
			for pump in pumps:
				print(str(pump.mlPerMin))
				totalMlPerMin += pump.mlPerMin
			 
			duration = self.pumpDuration(ingredient.amount, totalMlPerMin)
			
			print(str(ingredient.amount) + " " + str(totalMlPerMin) + " " + str(duration))
			
			for pump in pumps:
				pumpDevice = PumpControl(pump.gpioId)
				pumpDevice.runPumpAsync(duration)
	
	def pumpDuration(self, amount, mlPerMin):
		return amount / mlPerMin * 60
