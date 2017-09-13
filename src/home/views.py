"""
Homepage Views
"""
from django.views import generic

from .models import SemesterModule

class HomePageView(generic.ListView):
    """
    Homepage Index
    """
    template_name = 'home/landing_page.html'
    model = SemesterModule
    context_object_name = 'modules'
