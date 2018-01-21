from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.MembershipView.as_view(), name='membership_index'),
]
