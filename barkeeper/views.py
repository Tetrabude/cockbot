from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from barkeeper.models import Recipe

class IndexView(generic.ListView):
    template_name = 'barkeeper/index.html'
    context_object_name = 'recipe_list'
    
    def get_queryset(self):
        return Recipe.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'barkeeper/detail.html'
    
