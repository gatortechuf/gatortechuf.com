from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog_index'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name='blog_post'),
]