from django.db import models

class ResourceTag(models.Model):
    tag_name = models.CharField(max_length=256)


class Resource(models.Model):
    resource_url = models.CharField(max_length=256)
    resource_name = models.CharField(max_length=256)
    resource_image = models.FileField(max_length=256)
    resource_tag = models.ForeignKey(ResourceTag)