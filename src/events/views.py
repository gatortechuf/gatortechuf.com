"""
Events Views
"""
import json
from django.views import generic
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from .models import Event

class EventsView(generic.ListView):
    """
    Events Index
    """
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
    """
    Past Events
    """
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

class UpdateEvents(TemplateView):
    """
    Runs the FB JS sdk to update events
    """
    template_name = 'events/update.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateEvents, self).dispatch(*args, **kwargs)

def update_handler(request):
    """ Parses FB Events """
    try:
        loaded = json.loads(request.POST['events'])
    except Exception as exception:
        loaded = str(exception)

    for fb_event in loaded['events']:
        if 'place' in fb_event and 'name' in fb_event['place']:
            location = fb_event['place']['name']
        else:
            location = 'TBD'

        if 'description' in fb_event:
            description = fb_event['description']
        else:
            description = 'No Description'

        # Truncate the FB ID to fit in a postgres serial
        truncated_id = fb_event['id'] % 10000000

        event = Event.objects.update_or_create(id=truncated_id,
                                               slug=slugify(fb_event['name']),
                                               event_title=fb_event['name'],
                                               event_description=description,
                                               event_location_name=location,
                                               event_date=fb_event['start_time'],
                                               event_facebook_url='https://www.facebook.com/events/'
                                               + str(fb_event['id']))

    return HttpResponse('done')
