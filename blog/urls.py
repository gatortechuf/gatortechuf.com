from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog_index'),
    url(r'^archive/', views.ArchiveView.as_view(), name='blog_archive'),
    url(R'^suggest/', views.SuggestView.as_view(), name='blog_suggest'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name='blog_post'),
]