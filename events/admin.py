from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'event_location_name')
    search_fields = ('event_title', 'event_location_name', 'event_description')
    prepopulated_fields = {'slug': ('event_title',)}
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }
    fieldsets = [
        ('Title and Slug', {'fields': ('event_title', 'slug')}),
        ('Location and Time', {'fields': ('event_location_name', 'event_location_address', 'event_date')}),
        ('Description', {'fields': [('event_description')]})
    ]

admin.site.register(Event, EventAdmin)

