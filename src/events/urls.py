from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventsView.as_view(), name='event_index'),
]
