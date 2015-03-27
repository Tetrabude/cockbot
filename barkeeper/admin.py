from django.contrib import admin
from barkeeper.models import Pump, RawMaterial, Recipe, Ingredient, ExtraIngredient

admin.site.register(Pump)
admin.site.register(RawMaterial)

class IngredienInline(admin.StackedInline):
    model = Ingredient
    extra = 3

class ExtraIngredienInline(admin.StackedInline):
    model = ExtraIngredient
    extra = 3
    

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredienInline, ExtraIngredienInline]
    
admin.site.register(Recipe, RecipeAdmin)