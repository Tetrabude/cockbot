from barkeeper.models import Recipe, Ingredient

 

class Controller:
	def __init__(self, recipe):
		print "Cocktail: " + recipe.name
		
		for ingredient in recipe.ingredient_set.all() :
			print str(ingredient)
			
			pump = ingredient.rawMaterial.pump
			
			print str(pump)
			print str(self.pumpDuration(ingredient.amount, pump.mlPerMin))
			
	
	def pumpDuration(self, amount, mlPerMin):
		return amount * mlPerMin / 60