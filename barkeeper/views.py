from django.http import HttpResponse
from django.core.context_processors import request

def index(request):
    return HttpResponse("Cocktailliste")

def detail(request, recipe_id):
    return HttpResponse("Details zu Cocktail %s." % recipe_id)

