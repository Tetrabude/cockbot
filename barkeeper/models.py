from django.db import models

class Pump(models.Model):
    name = models.CharField(max_length=64)
    gpioId = models.IntegerField(default=0) 
    mlPerMin =  models.FloatField(default=0.0)
    
    def  __str__(self):
        return self.name + " " + str(self.gpioId) + " " + str(self.mlPerMin)
    
class RawMaterial(models.Model):
    name = models.CharField(max_length=64)
    pump = models.OneToOneField(Pump, null=True, blank=True)
    alcohol = models.BooleanField(default=True)
    
    def __str__(self):
        if self.pump is not None:   
            return self.name + " (" + self.pump.name + ")"
        else:
            return self.name + " (keine Pumpe)"
    
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=2048, default="")
    instruction = models.TextField(max_length=2048, default="")
    picture = models.URLField(max_length=256, default="")
    
    def isPumpable(self):
        if len(self.ingredient_set.all()) <= 0:
            return False
        
        for ingredient in self.ingredient_set.all():
            if ingredient.rawMaterial.pump is None:
                return False
            
        return True
    
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
  

    

    
