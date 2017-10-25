"""
Homepage Admin
"""
from django.contrib import admin

from django.db import models

from .models import HomePageHeader, HomePageButton, TextBlurb, SemesterModule

class ModuleAdmin(admin.ModelAdmin):
    """
    Homepage Admin
    """
    list_display = ('module_title',)

admin.site.register(SemesterModule, ModuleAdmin)
admin.site.register(HomePageHeader)
admin.site.register(HomePageButton)
admin.site.register(TextBlurb)