"""
Resource models
"""
from django.db import models

class Resource(models.Model):
    """
    Resource model
    """
    resource_name = models.CharField(max_length=256)
    resource_description = models.TextField("Description", max_length=2048)


class ResourceFile(models.Model):
    """
    Resource File Model
    """
    resource_parent = models.ForeignKey(Resource)
    resource_file_name = models.CharField(max_length=256)
    resource_file = models.FileField(max_length=1024)
