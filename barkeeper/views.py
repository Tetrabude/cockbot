from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from barkeeper.models import Recipe

def index(request):
    recipe_list = Recipe.objects.order_by('name')
    context = {'recipe_list': recipe_list}
    return render(request, 'barkeeper/index.html', context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'barkeeper/detail.html', {'recipe': recipe})

