from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$', views.EventsView.as_view(), name='event_index'),
    url(r'^archive/$', views.OldEventsView.as_view(), name='event_archive'),
    url(r'^update/$', views.UpdateEvents.as_view(), name='event_update'),
    url(r'^updater/$', views.update_handler, name='event_updater'),
]
