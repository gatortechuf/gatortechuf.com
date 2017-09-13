"""
Homepage Views
"""
from django.shortcuts import render

from .models import SemesterModule

class HomePageView(generic.ListView):
    """
    Homepage Index
    """
    template_name = 'home/landing_page.html'
    model = SemesterModule
    context_object_name = 'modules'
