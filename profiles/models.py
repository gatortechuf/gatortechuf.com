from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os


class Recruiter(models.Model):
    class Meta:
        permissions = (('directory_access', 'Can access member directories'),)


def upload_path(instance, filename):
    return os.path.join('resumes', '{}_{}_resume.pdf'.format(instance.user.first_name, instance.user.last_name))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    resume = models.FileField(default=None, upload_to=upload_path, null=True)
    phone_number = models.CharField(default=None, max_length=16, null=True)

    @property
    def username(self):
        return self.user.username

    @property
    def firstname(self):
        return self.user.first_name

    @property
    def lastname(self):
        return self.user.last_name

    @property
    def fullname(self):
        return self.user.get_full_name()




def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)

