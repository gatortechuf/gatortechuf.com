from django.db import models
from django.conf import settings


class CheckIn(models.Model):
    checked_in_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username