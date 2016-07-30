from django.shortcuts import render
from events.models import Event
from django.utils import timezone

def index(request):
    try:
        latest_event = Event.objects.filter(event_date__range=[timezone.now(), timezone.now() + timezone.timedelta(days=30)])[:1].get()
    except:
        latest_event = None
    context = { 'latest_event': latest_event }
    return render(request, 'home/landing_page.html', context)
