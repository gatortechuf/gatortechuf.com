from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.RecruiterView.as_view(), name='recruiters_index'),
]
