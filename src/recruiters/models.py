"""
Recruiter model
"""
from django.db import models

class RecuiterHeader(models.Model):
    """
    Header subtitle and email address
    """
    subtitle = models.CharField('Subtitle', max_length=1024)
    email_address = models.CharField('Email Button Address', max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email_address


class SponsorshipLevels(models.Model):
    """
    Different Sponsorship Packages
    """
    icon = models.CharField('Font Awesome Icon', max_length=128)
    title = models.CharField('Title', max_length=128)
    price = models.IntegerField('Price')
    details = models.TextField('Details', max_length=2048)

    def __str__(self):
        return self.title

class RecruiterLogo(models.Model):
    """
    Recruiter logos for sponsoring companies
    """
    logo_name = models.CharField('Company Name', max_length=128)
    url_name = models.CharField('Company URL', max_length=512)
    picture_name = models.ImageField('Company Image', blank=False, upload_to='logos')

    def __str__(self):
        return self.logo_name
