"""
Resources Views
"""
from django.views import generic

from .models import Resource

class ResourceView(generic.ListView):
    """
    Resources Index
    """
    template_name = 'resources/resources.html'
    model = Resource
    context_object_name = 'resources'
