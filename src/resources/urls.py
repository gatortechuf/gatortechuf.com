from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.ResourceView.as_view(), name='resource_index'),
]
