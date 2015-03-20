from django.test import TestCase
from barkeeper.models import Pump, RawMaterial, Recipe, Ingredient

class barkeeperTests(TestCase):
     
    def setUp(self):
        pumpA = Pump.objects.create(name="PumpA", gpioId=5, mlPerMin=40.0)
        
        orangeJuice = RawMaterial.objects.create(name="Orangensaft", pump=pumpA)
        coke = RawMaterial.objects.create(name="Cola")
        
        spezi = Recipe.objects.create(name="Spezi", description="Kalorienreduziert")
        
        Ingredient.objects.create(amount=150, recipe=spezi, rawMaterial=orangeJuice)
        Ingredient.objects.create(amount=150, recipe=spezi, rawMaterial=coke)

    def testPumpCanBeAccessed(self):
        """Database Pump"""
        pumpA = Pump.objects.get(name="PumpA")
        self.assertEqual(pumpA.name, "PumpA", "Name of pump not correct")
        self.assertEqual(pumpA.gpioId, 5, "GPIOID of pump not correct")
        self.assertEqual(pumpA.mlPerMin, 40.0, "Milliliter per Minute not correct")
        
        unic = pumpA.name + " " + str(pumpA.gpioId) + " " + str(pumpA.mlPerMin)
        self.assertEqual(str(pumpA), unic, "Unicodemethod not Correct")
        
    def testRawMaterialCanBeAccessed(self):
        """Database RawMaterial"""
        rawMaterialOrange = RawMaterial.objects.get(name="Orangensaft")
        self.assertEqual(rawMaterialOrange.name, "Orangensaft", "Wrong Raw Material")
        self.assertEqual(rawMaterialOrange.pump.name, "PumpA", "Wrong Pump")
        
        unic = rawMaterialOrange.name + " (" + rawMaterialOrange.pump.name + ")"
        self.assertEqual(str(rawMaterialOrange), unic, "Unicodemethod with pump not Correct")
        
        rawMaterialCoke = RawMaterial.objects.get(name="Cola")
        self.assertEqual(rawMaterialCoke.pump, None, "Pump should be Null")
        
        unic = rawMaterialCoke.name + " (keine Pumpe)"
        self.assertEqual(str(rawMaterialCoke), unic, "Unicodemethod no pump not Correct")
        
        
        
    def testRecipeCanBeAccessed(self):
        """Database Recipe"""
        recipe = Recipe.objects.get(name="Spezi")
        
        self.assertEqual(recipe.name, "Spezi", "Name of recipe not correct")
        self.assertEqual(recipe.description, "Kalorienreduziert", "Description of recipe not correct")
        
        self.assertEqual(str(recipe), recipe.name, "Unicodemethod not correct")
        
    def testIngredientCanBeAccessed(self): 
        """Database Ingredient"""
        recipe = Recipe.objects.get(name="Spezi")
        ingredient = recipe.ingredient_set.filter(rawMaterial__name="Cola")
        
        self.assertEqual(ingredient[0].recipe, recipe, "Wrong Recipe")
        self.assertEqual(ingredient[0].amount, 150, "Wrong Amount")
        self.assertEqual(ingredient[0].rawMaterial.name, "Cola", "Wrong rawMaterial")
        
        unic = str(ingredient[0].amount) + ' ml ' + str(ingredient[0].rawMaterial)
        self.assertEqual(str(ingredient[0]), unic, "Unicodemethod not correct")
        
        