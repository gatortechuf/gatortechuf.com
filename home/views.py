from django.shortcuts import render
from events.models import Event
from django.utils.timezone import datetime, timedelta

def index(request):
    latest_event = Event.objects.filter(event_date__range=[datetime.now(), datetime.today() + timedelta(days=100)])[:1].get()
    context = { 'latest_event': latest_event }
    return render(request, 'home/landing_page.html', context)

