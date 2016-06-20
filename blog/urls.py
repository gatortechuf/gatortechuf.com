from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.BlogPostView.as_view(), name='blogpostview'),
    url(r'^add_comment/$', views.CommentView.as_view(), name='formview'),
]