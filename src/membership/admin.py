"""
Membership Admin
"""
from django.contrib import admin

from .models import Leader, Coordinator

class LeaderAdmin(admin.ModelAdmin):
    """
    Executive Board Member Admin
    """
    list_display = ('leader_name',)

class CoordinatorAdmin(admin.ModelAdmin):
    """
    Coordinator Admin
    """
    list_display = ('coordinator_name',)

admin.site.register(Leader, LeaderAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)
