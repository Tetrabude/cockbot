from hardware.PumpControlPi import PumpControlPi as PumpControl

class Controller:
	def __init__(self, recipe):
		print("Cocktail: " + recipe.name)
		
		if not recipe.isPumpable():
			raise NameError("Nicht alle Zutaten sind an Pumpen angeschlossen")
		
		for ingredient in recipe.ingredient_set.all() :
			print(str(ingredient))
			
			pump = ingredient.rawMaterial.pump
			
			print(str(pump))
			pumpDevice = PumpControl(pump.gpioId)
			
			duration = self.pumpDuration(ingredient.amount, pump.mlPerMin)
			print(str(duration))
			pumpDevice.runPumpAsync(duration)
	
	def pumpDuration(self, amount, mlPerMin):
		return amount * mlPerMin / 60
