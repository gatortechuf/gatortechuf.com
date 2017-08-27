from django.db import models

#class ResourceTag(models.Model):
#    tag_name = models.CharField(max_length=256)


#class Resource(models.Model):
#    resource_url = models.CharField(max_length=256, default=None, blank=True, null=True)
#    resource_name = models.CharField(max_length=256, default=None, blank=True, null=True)
#    resource_image = models.FileField(max_length=256, default=None, blank=True, null=True)
#    resource_tag = models.ForeignKey(ResourceTag, default=None, blank=True, null=True)

class Meeting(models.Model):
    meeting_name = models.CharField('Meeting Title', max_length=256)
    meeting_photo = models.ImageField(blank=True, upload_to='meeting_photos')
    meeting_time = models.DateTimeField()
    meeting_description = models.TextField('Desciption', max_length=2048)
    meeting_files = models.FileField(blank=True, upload_to='meeting_files')

    def __str__(self):
        return self.meeting_name

    class Meta:
        verbose_name = 'Meeting'
        verbose_name_plural = 'Meetings'

class Workshop(models.Model):
    workshop_name = models.CharField('Workshop Title', max_length=256)
    workshop_photo = models.ImageField(blank=True, upload_to='workshop_photos')
    workshop_time = models.DateTimeField()
    workshop_description = models.TextField('Desciption', max_length=2048)
    workshop_link = models.CharField('Workshop Link', max_length=256)

    def __str__(self):
        return self.workshop_name

    class Meta:
        verbose_name = 'Workshop'
        verbose_name_plural = 'Workshops'
