from django.contrib import admin

from django.db import models

from .models import Leader, Coordinator

class LeaderAdmin(admin.ModelAdmin):
    list_display = ('leader_name',)

class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('coordinator_name',)

admin.site.register(Leader, LeaderAdmin)
admin.site.register(Coordinator, CoordinatorAdmin)
