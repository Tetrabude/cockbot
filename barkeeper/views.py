from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from barkeeper.models import Recipe, Pump
from django.core.urlresolvers import reverse

from logic.Controller import Controller
from logic.CleaningController import CleaningController

class IndexView(generic.ListView):
    template_name = 'barkeeper/index.html'
    context_object_name = 'recipe_list'
    
    def get_queryset(self):
        return Recipe.objects.all().exclude(ingredient__rawMaterial__pump=None).order_by('name')

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'barkeeper/detail.html'
    
def start(request, pk):
    recipe = Recipe.objects.get(pk=pk)  
    try:  
        tmp = Controller(recipe)
        duration = tmp.start()
        
        context = {'recipe': recipe, 'duration': duration}
        return render(request, 'barkeeper/start.html', context)
        #return HttpResponse("Pumpen " + pk)
    except NameError as e:
        return HttpResponse("Error: " + str(e))
    
    
class PumpsIndexView(generic.ListView):
    template_name = 'barkeeper/admin/index.html'
    context_object_name = 'pump_list'
    
    def get_queryset(self):
        return Pump.objects.all()
    
    
def clean(request):
    key = request.POST['pump']
    duration = float(request.POST['duration'])
    pump = get_object_or_404(Pump, pk=key)

    tmp = CleaningController()
    tmp.start(pump, duration)
    
    return HttpResponseRedirect(reverse('pumpIndex'))
