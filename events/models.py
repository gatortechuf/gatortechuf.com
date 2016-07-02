from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=128)
    event_description = models.TextField(max_length=768)
    event_location_name = models.CharField(max_length=256, default='Heavener Hall 250')
    event_location_address = models.CharField(max_length=256, default='1325 W University Ave, Gainesville, FL 32601')
    event_date = models.DateTimeField('event date', auto_now=False)
    slug = models.SlugField(default=None, unique=True, max_length=128)

    def __str__(self):
        return self.event_title
