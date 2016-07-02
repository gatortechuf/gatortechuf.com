from django.db import models

class Event(models.Model):
    event_title = models.CharField(max_length=128)
    event_description = models.CharField(max_length=768)
    event_location = models.CharField(max_length=256, default='Heavener Hall 250')
    event_date = models.DateTimeField('event date', auto_now=False)

    def __str__(self):
        return self.event_title
