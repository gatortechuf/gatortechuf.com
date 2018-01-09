"""
Resources Admin
"""
from django.contrib import admin
from .models import Resource, ResourceFile, ResourceLink, ResourceImage

admin.site.register(Resource)
admin.site.register(ResourceFile)
admin.site.register(ResourceLink)
admin.site.register(ResourceImage)
