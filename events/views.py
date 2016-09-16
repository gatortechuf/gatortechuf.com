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

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        return context


class OldEventsView(generic.ListView):
    template_name = 'events/old_events.html'
    model = Event
    context_object_name = 'old_event_list'

    def get_queryset(self):
        return Event.objects.filter(
            event_date__lt=timezone.now()
        ).order_by('-event_date')

    def get_context_data(self, **kwargs):
        context = super(OldEventsView, self).get_context_data(**kwargs)
        return context
