from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventsView.as_view(), name='event_index'),
    url(r'^archive/$', views.OldEventsView.as_view(), name='event_archive'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailedEventView.as_view(), name='event_detail'),
]