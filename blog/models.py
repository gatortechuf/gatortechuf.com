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
    comment_content = models.CharField(max_length=1024)
    comment_date = models.DateTimeField('date posted', auto_now=True)
    comment_author = models.ForeignKey(User)
    comment_blog_post = models.ForeignKey(BlogPost, related_name='comments')

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ['-comment_date']


class SuggestedPost(models.Model):
    topic_idea = models.TextField(max_length=512, default='None', null=False)
    topic_author = models.ForeignKey(User)
    topic_date = models.DateTimeField('date suggested', auto_now=True)

    def __str__(self):
        return self.topic_author.get_full_name()
