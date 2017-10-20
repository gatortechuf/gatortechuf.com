"""
Recuiters Admin
"""
from django.contrib import admin

from .models import RecruiterHeader, RecruiterLogo, SponsorshipLevels
admin.site.register(RecruiterHeader)
admin.site.register(SponsorshipLevels)
admin.site.register(RecruiterLogo)
