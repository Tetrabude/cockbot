from django.db import models

    
class RawMaterial(models.Model):
    name = models.CharField(max_length=64)
    #pump = models.OneToOneField(Pump, null=True, blank=True)
    alcohol = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Pump(models.Model):
    name = models.CharField(max_length=64)
    gpioId = models.IntegerField(default=0) 
    mlPerMin =  models.FloatField(default=0.0)
    rawMaterial = models.ForeignKey(RawMaterial, null=True, blank=True)
    
    def  __str__(self):
        base = self.name + ", GPIO " + str(self.gpioId) + ", " + str(self.mlPerMin) + " ml/min"
        if(self.rawMaterial is not None):
            base += ", " + self.rawMaterial.name
        return base


class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=2048, default="", null=True, blank=True)
    instruction = models.TextField(max_length=2048, default="", null=True, blank=True)
    picture = models.URLField(max_length=256, default="", null=True, blank=True)
    
    def isPumpable(self):
        
        ingredients = self.ingredient_set.all()
        
        if len(ingredients) <= 0:
            return False
        
        for ingredient in ingredients:
            if len(ingredient.rawMaterial.pump_set.all()) <= 0:
                return False
            
        return True
    
    def isAlcohol(self):
        for ingredient in self.ingredient_set.all():
            if(ingredient.rawMaterial.alcohol):
                return True
        return False
    isAlcohol.boolean = True
    
    def amount(self):
        totalAmount = 0
        for ingredient in self.ingredient_set.all():
            totalAmount += ingredient.amount
        return totalAmount
    
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(Recipe) 
    rawMaterial = models.ForeignKey(RawMaterial)
    
    def __str__(self):
        return str(self.amount) + ' ml ' + str(self.rawMaterial)


class ExtraIngredient(models.Model):
    amount = models.CharField(max_length=56)
    recipe = models.ForeignKey(Recipe) 
    rawMaterial = models.CharField(max_length=56)
    
    def __str__(self):
        return str(self.amount) + ' ' + str(self.rawMaterial)

