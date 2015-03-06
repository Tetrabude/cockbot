from django.contrib import admin
from barkeeper.models import Pump, RawMaterial, Recipe, Ingredient

admin.site.register(Pump)
admin.site.register(RawMaterial)

class IngredienInline(admin.StackedInline):
    model = Ingredient
    extra = 3
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredienInline]
    
admin.site.register(Recipe, RecipeAdmin)