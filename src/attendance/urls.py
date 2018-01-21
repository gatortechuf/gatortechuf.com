from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.index, name='attendance_index'),
    path('update/', views.checkin, name='attendance_checkin')
]
