from django.db import models

# Create your models here.
class RecruiterLogo(models.Model):
    logo_name = models.CharField("Company Name", max_length = 128)
    url_name = models.CharField("Company URL", max_length = 512)
    picture_name = models.ImageField("Company Image", blank = False, upload_to = "logos")

    def __str__(self):
        return self.logo_name