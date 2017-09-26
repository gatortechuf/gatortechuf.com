"""
Events Admin
"""
from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import Calendar

class CalendarAdmin(admin.ModelAdmin):
    """
    Calendar Admin
    """
    list_display = ('calendar_id',)

admin.site.register(Calendar, CalendarAdmin)
