"""
Homepage models
"""
from django.db import models

class HomePageHeader(models.Model):
    """
    Header underneath homepage logo
    """
    subtitle = models.TextField('Subtitle', max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subtitle

class HomePageButton(models.Model):
    """
    Button row
    """
    icon = models.CharField('Font Awesome Icon', max_length=128)
    button_text = models.CharField('Button Text', max_length=128)
    button_link = models.CharField('Button Link', max_length=1024)
    
class TextBlurb(models.Model):
    """
    Blocks that appear between semester modules and header buttons
    """
    icon = models.CharField('Font Awesome Icon', max_length=128)
    blurb_title = models.CharField('Blurb Title', max_length=128)
    blurb_text = models.CharField('Blurb Text', max_length=512)

class SemesterModule(models.Model):
    """
    SemesterModule contains the title, description, and icon for the
    "Modules for this semester" section
    """
    module_title = models.CharField('Title', max_length=256)
    module_icon = models.CharField('Font Awesome Icon', max_length=128)
    module_description = models.TextField('Description', max_length=1024)