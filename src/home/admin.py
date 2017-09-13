"""
Homepage Admin
"""
from django.contrib import admin

from django.db import models

from .models import SemesterModule

class ModuleAdmin(admin.ModelAdmin):
    """
    Homepage Admin
    """
    list_display = ('module_title',)

admin.site.register(SemesterModule, ModuleAdmin)
