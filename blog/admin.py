from django.contrib import admin

from .models import BlogPost, BlogComment

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogComment)