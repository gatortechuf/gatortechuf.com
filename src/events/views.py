"""
Events Views
"""
from django.views import generic

from .models import Calendar

class EventsView(generic.ListView):
    """
    Events Index
    """
    template_name = 'events/events.html'
    model = Calendar
    context_object_name = 'calendar'

    def get_queryset(self):
        return Calendar.objects.all()[:1].get()
