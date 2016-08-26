from django.views import generic
from django.utils import timezone

from .models import Event, EventTag

class EventsView(generic.ListView):
    template_name = 'events/events.html'
    model = Event
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.filter(
            event_date__gte=timezone.now()
        ).order_by('-event_date')

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        context['event_tags'] = EventTag.objects.all()
        return context


class FilteredEventsView(generic.ListView):
    template_name = 'events/filter.html'
    model = Event
    context_object_name = 'filtered_event_list'

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        return Event.objects.filter(
            event_date__gte=timezone.now()
        ).filter(
            event_tag_id__exact=tag_id
        ).order_by('event_date')

    def get_context_data(self, **kwargs):
        context = super(FilteredEventsView, self).get_context_data(**kwargs)
        context['event_tags'] = EventTag.objects.all()
        context['tag_id'] = int(self.kwargs['tag_id'])
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
        context['event_tags'] = EventTag.objects.all()
        return context


class OldFilteredEventsView(generic.ListView):
    template_name = 'events/old_filter.html'
    model = Event
    context_object_name = 'filtered_event_list'

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        return Event.objects.filter(
            event_date__lt=timezone.now()
        ).filter(
            event_tag_id__exact=tag_id
        ).order_by('event_date')

    def get_context_data(self, **kwargs):
        context = super(OldFilteredEventsView, self).get_context_data(**kwargs)
        context['event_tags'] = EventTag.objects.all()
        context['tag_id'] = int(self.kwargs['tag_id'])
        return context



class DetailedEventView(generic.DetailView):
    template_name = 'events/details.html'
    model = Event