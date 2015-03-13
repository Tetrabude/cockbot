from barkeeper.models import Recipe
 

class Controller:
	def __init__(self, recipe):
		self.recipe = recipe
		print "Cocktail: " + recipe.name