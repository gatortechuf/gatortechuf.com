from django.urls import path
from . import views

app_name = 'recruiters'

urlpatterns = [
    path('', views.RecruiterView.as_view(), name='recruiters_index'),
]
