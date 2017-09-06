"""
Recruiter model
"""
from django.db import models

class RecruiterLogo(models.Model):
    """
    Recruiter logos for sponsoring companies
    """
    logo_name = models.CharField("Company Name", max_length=128)
    url_name = models.CharField("Company URL", max_length=512)
    picture_name = models.ImageField("Company Image", blank=False, upload_to="logos")

    def __str__(self):
        return self.logo_name
