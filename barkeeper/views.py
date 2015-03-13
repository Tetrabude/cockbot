from django.http import HttpResponse
from django.core.context_processors import request
from barkeeper.models import Recipe

def index(request):
    recipe_list = Recipe.objects.order_by('name')
    output = '<br>'.join([p.name for p in recipe_list])
    return HttpResponse(output)

def detail(request, recipe_id):
    return HttpResponse("Details zu Cocktail %s." % recipe_id)

