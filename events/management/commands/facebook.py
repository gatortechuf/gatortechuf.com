import os
import requests
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from events.models import Event

class Command(BaseCommand):
    help = 'Updates website events from Facebook'

    def facebook_event_url(self, id):
        return 'https://www.facebook.com/events/' + str(id)

    def handle(self, *args, **options):
        events_json = requests.get('https://graph.facebook.com/v2.7/gatortechuf/events?limit=2&access_token=' + os.getenv('FB_ID') + '|' + os.getenv('FB_SECRET')).json()

        for fb_event in events_json['data']:
            if 'place' in fb_event and 'name' in fb_event['place']:
                location = fb_event['place']['name']
            else:
                location = 'TBD'

            if 'description' in fb_event:
                description = fb_event['description']
            else:
                description = 'No Description'

            try:
                event, created = Event.objects.update_or_create(id=fb_event['id'],
                                                                slug=slugify(fb_event['name']),
                                                                event_title=fb_event['name'],
                                                                event_description=description,
                                                                event_location_name=location,
                                                                event_date=fb_event['start_time'],
                                                                event_facebook_url=self.facebook_event_url(fb_event['id']))
            except:
                raise CommandError('Missing key')

            event.opened = False
            event.save()

        self.stdout.write(self.style.SUCCESS('Updated Facebook Events'))
