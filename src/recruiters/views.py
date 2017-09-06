# from django.shortcuts import render
from django.views import generic
from .models import RecruiterLogo
# Create your views here.
# def index(request):
#   return render(request, 'recruiters/recruiters.html')
class RecruiterView(generic.ListView):
    template_name = "recruiters/recruiters.html"
    model = RecruiterLogo
    context_object_name = "logos"
    