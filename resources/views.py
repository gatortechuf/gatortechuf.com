from django.views import generic

from .models import Resource

class ResourceView(generic.ListView):
    template_name = 'resources/resources.html'
    model = Resource

