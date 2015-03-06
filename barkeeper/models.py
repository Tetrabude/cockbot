from django.db import models

class Pump(models.Model):
    name = models.CharField(max_length=64)  
    
class RawMaterial(models.Model):
    name = models.CharField(max_length=64)
    pump = models.OneToOneField(Pump, blank=True)
    
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
    
class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(Recipe) 
    rawMaterial = models.ForeignKey(RawMaterial)




  

    

    
