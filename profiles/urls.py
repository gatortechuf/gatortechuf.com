from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProfileList.as_view(), name='profile_list'),
    url(r'^(?P<pk>\d+)/$', views.Profile.as_view(), name='profile_index'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditProfile.as_view(), name='profile_edit'),
    url(r'^search/$', views.SearchProfile.as_view(), name='profile_search')
]
