"""
Recuiters Admin
"""
from django.contrib import admin

from .models import RecruiterHeader, RecruiterLogo, SponsorshipLevel
admin.site.register(RecruiterHeader)
admin.site.register(SponsorshipLevel)
admin.site.register(RecruiterLogo)
