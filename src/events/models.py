"""
Events Model
"""
from django.db import models

class Calendar(models.Model):
    """
    Google Calendar Embed
    """
    calendar_id = models.CharField('Calendar ID', max_length=1024)

    class Meta:
        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendars'
