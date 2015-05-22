from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from barkeeper.models import Recipe

from logic.Controller import Controller

class IndexView(generic.ListView):
    template_name = 'barkeeper/index.html'
    context_object_name = 'recipe_list'
    
    def get_queryset(self):
        return Recipe.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'barkeeper/detail.html'
    
def start(request, pk):
    recipe = Recipe.objects.get(pk=pk)  
    try:  
        Controller(recipe)
        context = {'recipe': recipe}
        return render(request, 'barkeeper/start.html', context)
        #return HttpResponse("Pumpen " + pk)
    except NameError as e:
        return HttpResponse("Error: " + str(e))