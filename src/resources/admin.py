"""
Resources Admin
"""
from django.contrib import admin
from .models import Resource, ResourceFile

admin.site.register(Resource)
admin.site.register(ResourceFile)
