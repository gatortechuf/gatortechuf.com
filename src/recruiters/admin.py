"""
Recuiters Admin
"""
from django.contrib import admin

from .models import RecuiterHeader, RecruiterLogo, SponsorshipLevels
admin.site.register(RecuiterHeader)
admin.site.register(SponsorshipLevels)
admin.site.register(RecruiterLogo)
