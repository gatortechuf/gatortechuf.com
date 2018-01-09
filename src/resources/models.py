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

    def __str__(self):
        return self.resource_name


class ResourceFile(models.Model):
    """
    Resource File Model
    """
    resource_parent = models.ForeignKey(Resource)
    resource_file_name = models.CharField(max_length=256)
    resource_file = models.FileField(max_length=1024, upload_to='resources')

    def __str__(self):
        return self.resource_file_name

class ResourceLink(models.Model):
    """
    Resource Link Model
    """
    resource_parent = models.ForeignKey(Resource)
    resource_link = models.CharField(max_length=1024)
    resource_link_name = models.CharField(max_length=256)

    def __str__(self):
        return self.resource_link_name


class ResourceImage(models.Model):
    """
    Resource Header Image
    """
    resource_parent = models.ForeignKey(Resource)
    resource_image = models.ImageField(upload_to='resource_images')