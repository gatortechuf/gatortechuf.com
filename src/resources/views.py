from django.shortcuts import render
from django.views import generic

from .models import Resource

class ResourceView(generic.ListView):
    template_name = 'resources/resources.html'
    model = Resource

def workshop(request):
    return render(request, 'resources/workshop.html')

