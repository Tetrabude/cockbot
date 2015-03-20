from django.db import models

class Pump(models.Model):
    name = models.CharField(max_length=64)
    gpioId = models.IntegerField(default=0) 
    mlPerMin =  models.FloatField(default=0.0)
    
    def __unicode__(self):
        return self.name + " " + str(self.gpioId) + " " + str(self.mlPerMin)
    
class RawMaterial(models.Model):
    name = models.CharField(max_length=64)
    pump = models.OneToOneField(Pump, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=2048)
    
    def __unicode__(self):
        return self.name
    
class Ingredient(models.Model):
    amount = models.FloatField()
    recipe = models.ForeignKey(Recipe) 
    rawMaterial = models.ForeignKey(RawMaterial)
    
    def __unicode__(self):
        return str(self.amount) + ' ml' + str(self.rawMaterial)



  

    

    
