try:
	import RPi.GPIO as GPIO
	from hardware.PumpControlPi import PumpControlPi as PumpControl
	print("Pi loaded")
except ImportError:
	from hardware.PumpControlMock import PumpControlMock as PumpControl
	print("Mock loaded")

class Controller:
	def __init__(self, recipe):
		self.recipe = recipe
		
	def start(self):
		print("Cocktail: " + self.recipe.name)
		if not self.recipe.isPumpable():
			raise NameError("Nicht alle Zutaten sind an Pumpen angeschlossen")
		
		maxDuration = 0
		
		for ingredient in self.recipe.ingredient_set.all() :
			print(str(ingredient))
			
			pumps = ingredient.rawMaterial.pump_set.all()
			
			totalMlPerMin = 0.0
			for pump in pumps:
				print(str(pump.mlPerMin))
				totalMlPerMin += pump.mlPerMin
			
			duration = self.pumpDuration(ingredient.amount, totalMlPerMin)
			
			if(duration > maxDuration):
				maxDuration = duration
			
			print(str(ingredient.amount) + " " + str(totalMlPerMin) + " " + str(duration))
			
			for pump in pumps:
				pumpDevice = PumpControl(pump.gpioId)
				pumpDevice.runPumpAsync(duration)
			
		return maxDuration
	
	def pumpDuration(self, amount, mlPerMin):
		return amount / mlPerMin * 60
