from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'home/index.html')

