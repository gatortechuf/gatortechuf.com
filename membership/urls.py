from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MembershipView.as_view(), name='membership_index'),
]
