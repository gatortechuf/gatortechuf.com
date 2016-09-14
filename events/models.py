from django.db import models

class EventTag(models.Model):
    event_tag = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Event Tag'
        verbose_name_plural = 'Event Tags'

    def __str__(self):
        return self.event_tag

class Event(models.Model):
    event_title = models.CharField('Title', max_length=128)
    event_description = models.TextField('Description', max_length=768)
    event_location_name = models.CharField('Location Name', max_length=256, default='Heavener Hall 270')
    event_facebook_url = models.CharField('Facebook Event URL', max_length=256)
    event_date = models.DateTimeField('Date', auto_now=False)
    slug = models.SlugField('URL (Avoid Editing)', default=None, unique=True, max_length=128)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


