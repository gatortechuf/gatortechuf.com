from django.db import models

class SemesterModule(models.Model):
    module_title = models.CharField('Title', max_length=256)
    module_icon = models.CharField('Font Awesome Icon', max_length=128)
    module_description = models.TextField('Description', max_length=1024)
