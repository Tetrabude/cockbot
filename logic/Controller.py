try:
	import RPi.GPIO as GPIO
	from hardware.PumpControlPi import PumpControlPi as PumpControl
	print("Pi loaded")
except ImportError:
	from hardware.PumpControlMock import PumpControlMock as PumpControl
	print("Mock loaded")

import logging

drinkinglog = logging.getLogger('drinkinglog')

class Controller:
	def __init__(self, recipe):
		self.recipe = recipe
		
	def start(self):
		print("Cocktail: " + self.recipe.name)
		drinkinglog.info(self.recipe.name)
		if not self.recipe.isPumpable():
			raise NameError("Nicht alle Zutaten sind an Pumpen angeschlossen")
		
		maxDuration = 0
		
		recipeAmount = self.recipe.amount()
		
		maxAmount = 200.0
		amountFactor = 1.0
		
		if recipeAmount > maxAmount:
			amountFactor = maxAmount / recipeAmount 
			
		print(str(maxAmount) + " " + str(recipeAmount) + " " + str(amountFactor))
			
		
		for ingredient in self.recipe.ingredient_set.all() :
			print(str(ingredient))
			
			pumps = ingredient.rawMaterial.pump_set.all()
			
			totalMlPerMin = 0.0
			for pump in pumps:
				print(str(pump.mlPerMin))
				totalMlPerMin += pump.mlPerMin
			
			duration = self.pumpDuration(ingredient.amount * amountFactor, totalMlPerMin)
			
			if(duration > maxDuration):
				maxDuration = duration
			
			print("Amount: " + str(ingredient.amount) + " AmountMitFaktor " + str(ingredient.amount * amountFactor) + " " + str(totalMlPerMin) + " " + str(duration))
			
			for pump in pumps:
				pumpDevice = PumpControl(pump.gpioId)
				pumpDevice.runPumpAsync(duration)
			
		return maxDuration
	
	def pumpDuration(self, amount, mlPerMin):
		return amount / mlPerMin * 60
