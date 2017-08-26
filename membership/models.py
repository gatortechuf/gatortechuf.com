import os
from django.db import models
from django.conf import settings

class Leader(models.Model):
    leader_title = models.CharField('Leadership Title', max_length=128)
    leader_image = models.ImageField(blank=True, upload_to='membership')
    leader_name = models.CharField('Name', max_length=256)
    leadership_bio = models.TextField('Bio', max_length=2048)

    def __str__(self):
        return self.leader_name

    class Meta:
        verbose_name = 'Leader'
        verbose_name_plural = 'Leaders'


class Coordinator(models.Model):
    coordinator_title = models.CharField('Coordinator Title', max_length=128)
    coordinator_name = models.CharField('Name', max_length=256)
    coordinator_image = models.ImageField(blank=True, upload_to='membership')
    coordinator_bio = models.TextField('Bio', max_length=2048, default='bio')
    coordinator_leader = models.ForeignKey(Leader, on_delete=models.CASCADE)

    def __str__(self):
        return self.coordinator_name

    class Meta:
        verbose_name = 'Coordinator'
        verbose_name_plural = 'Coordinators'
