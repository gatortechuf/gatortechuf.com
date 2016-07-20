from django.shortcuts import render
from events.models import Event
from django.utils.timezone import datetime, timedelta

def index(request):
    try:
        latest_event = Event.objects.filter(event_date__range=[datetime.now(), datetime.today() + timedelta(days=30)])[:1].get()
    except:
        latest_event = None
    context = { 'latest_event': latest_event }
    return render(request, 'home/landing_page.html', context)
