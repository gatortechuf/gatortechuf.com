from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    blog_title = models.CharField('Title', max_length=200)
    post_date = models.DateTimeField('Post Date', auto_now=True)
    blog_author = models.ForeignKey(User, verbose_name='Author')
    blog_content = models.TextField('Post', max_length=10000)
    slug = models.SlugField('URL (Avoid Editing)', default=None, unique=True, max_length=128)

    class Meta:
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.blog_title


class BlogComment(models.Model):
    comment_content = models.CharField(max_length=1024)
    comment_date = models.DateTimeField('date posted', auto_now=True)
    comment_author = models.ForeignKey(User)
    comment_blog_post = models.ForeignKey(BlogPost, related_name='comments')

    class Meta:
        ordering = ['-comment_date']
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return self.comment_content


class SuggestedPost(models.Model):
    topic_idea = models.TextField('Suggestion', max_length=512, null=False)
    topic_author = models.ForeignKey(User, verbose_name='Suggested By')
    topic_date = models.DateTimeField('Date Suggested', auto_now=True)

    class Meta:
        verbose_name = 'Suggested Topic'
        verbose_name_plural = 'Suggested Topics'

    def __str__(self):
        return self.topic_author.get_full_name()
