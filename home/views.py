from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/landing_page.html')

