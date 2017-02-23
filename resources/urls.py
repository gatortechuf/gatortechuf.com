from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ResourceView.as_view(), name='resource_index'),
    url(r'^workshop/$', views.workshop, name='workshop'),
]
