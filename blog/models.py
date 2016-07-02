from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=200)
    post_date = models.DateTimeField('date posted', auto_now=True)
    blog_author = models.ForeignKey(User)
    blog_content = models.TextField(max_length=10000)
    slug = models.SlugField(default=None, unique=True, max_length=128)

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=1000)
    comment_date = models.DateTimeField('date posted', auto_now=True)
    comment_author = models.ForeignKey(User)

    def __str__(self):
        return self.comment_text