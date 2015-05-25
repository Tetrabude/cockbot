from django.contrib import admin
from barkeeper.models import Pump, RawMaterial, Recipe, Ingredient, ExtraIngredient

class PumpAdmin(admin.ModelAdmin):
    list_display = ('name', 'gpioId', 'mlPerMin', 'rawMaterial')
    
admin.site.register(Pump, PumpAdmin)
#admin.site.register(RawMaterial)

class IngredienInline(admin.StackedInline):
    model = Ingredient
    extra = 3

class ExtraIngredienInline(admin.StackedInline):
    model = ExtraIngredient
    extra = 3

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredienInline, ExtraIngredienInline]
    list_display = ('name', 'rawMaterials')
    
    def rawMaterials(self, obj):
        rawMaterialsNames = []
        for ingredient in obj.ingredient_set.all():
            rawMaterialsNames.append(ingredient.rawMaterial.name)
        return ", ".join(rawMaterialsNames)
    
admin.site.register(Recipe, RecipeAdmin)


class PumpInline(admin.StackedInline):
    model = Pump
    extra = 0

class RawMaterialAdmin(admin.ModelAdmin):
    inlines = [PumpInline]
    list_display = ('name', 'alcohol', 'recipes', 'pumps')

    def recipes(self, obj):
        recipeNames = []
        for ingredient in obj.ingredient_set.all():
            recipeNames.append(ingredient.recipe.name)
        return ", ".join(recipeNames)
    
    def pumps(self, obj):
        pumpNames = []
        for pump in obj.pump_set.all():
            pumpNames.append(pump.name)
        return ", ".join(pumpNames)
        
admin.site.register(RawMaterial, RawMaterialAdmin)
