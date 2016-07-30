from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EventsView.as_view(), name='event_index'),
    url(r'^filter/(?P<tag_id>[\d]+)/$', views.FilteredEventsView.as_view(), name='event_filter'),
    url(r'^archive/$', views.OldEventsView.as_view(), name='event_archive'),
    url(r'^archive/filter/(?P<tag_id>[\d]+)/$', views.OldFilteredEventsView.as_view(), name='archive_event_filter'),
    url(r'^(?P<slug>[\w-]+)/$', views.DetailedEventView.as_view(), name='event_detail'),
]