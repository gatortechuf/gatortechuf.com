from django.db import models

class ResourceTag(models.Model):
    tag_name = models.CharField(max_length=256)


class Resource(models.Model):
    resource_url = models.CharField(max_length=256, default=None, blank=True, null=True)
    resource_name = models.CharField(max_length=256, default=None, blank=True, null=True)
    resource_image = models.FileField(max_length=256, default=None, blank=True, null=True)
    resource_tag = models.ForeignKey(ResourceTag, default=None, blank=True, null=True)
