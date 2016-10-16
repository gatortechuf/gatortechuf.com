from django.contrib import admin
from .models import Resource, ResourceTag

admin.site.register(Resource)
admin.site.register(ResourceTag)