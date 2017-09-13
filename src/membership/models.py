"""
Membership page model, which contains the executive board and their coordinators
"""
from django.db import models

class Leader(models.Model):
    """
    Executive board member and their name, photo, and biography
    """
    leader_title = models.CharField('Leadership Title', max_length=128)
    leader_image = models.ImageField(blank=True, upload_to='membership')
    leader_name = models.CharField('Name', max_length=256)
    leadership_bio = models.TextField('Bio', max_length=2048)

    def __str__(self):
        return self.leader_name

    class Meta:
        """ Meta Class for admin interface names """
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'


class Coordinator(models.Model):
    """
    Coordinator and their name, photo, and biography
    """
    coordinator_title = models.CharField('Coordinator Title', max_length=128)
    coordinator_name = models.CharField('Name', max_length=256)
    coordinator_image = models.ImageField(blank=True, upload_to='membership')
    coordinator_bio = models.TextField('Bio', max_length=2048, default='bio')
    coordinator_leader = models.ForeignKey(Leader, on_delete=models.CASCADE)

    def __str__(self):
        return self.coordinator_name

    class Meta:
        """ Meta Class for admin interface names """
        verbose_name = 'Coordinator'
        verbose_name_plural = 'Coordinators'
