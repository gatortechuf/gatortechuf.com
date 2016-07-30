from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='blog_index'),
    url(r'^archive/', views.ArchiveView.as_view(), name='blog_archive'),
    url(r'^suggest/', views.SuggestView.as_view(), name='blog_suggest'),
    url(r'^comment/', views.CommentView.as_view(), name='blog_comment'),
    url(r'^(?P<slug>[\w-]+)/$', views.BlogPostView.as_view(), name='blog_post'),
]