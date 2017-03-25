from django.shortcuts import render
from django.views import generic

from .models import SemesterModule

class HomePageView(generic.ListView):
    template_name = 'home/landing_page.html'
    model = SemesterModule
    context_object_name = 'modules'
