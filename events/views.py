from django.views import generic
from django.utils import timezone

from .models import Event

class EventsView(generic.ListView):
    template_name = 'events/events.html'
    model = Event
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.filter(
            event_date__gte=timezone.now()
        ).order_by('event_date')


class OldEventsView(generic.ListView):
    template_name = 'events/old_events.html'
    model = Event
    context_object_name = 'old_event_list'

    def get_queryset(self):
        return Event.objects.filter(
            event_date__lt=timezone.now()
        ).order_by('event_date')


class DetailedEventView(generic.DetailView):
    template_name = 'events/details.html'
    model = Event