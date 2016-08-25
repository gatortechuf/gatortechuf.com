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
    event_location_name = models.CharField('Location Name', max_length=256, default='Heavener Hall 250')
    #event_location_address = models.CharField('Address', max_length=256, default='1325 W University Ave, Gainesville, FL 32601')
    event_date = models.DateTimeField('Date', auto_now=False)
    #event_tag = models.ForeignKey(EventTag, default=1, verbose_name='Tag')
    slug = models.SlugField('URL (Avoid Editing)', default=None, unique=True, max_length=128)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'


