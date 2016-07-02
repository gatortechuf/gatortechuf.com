from django.contrib import admin

from .models import BlogPost, BlogComment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_author')
    search_fields = ('blog_title', 'blog_content')
    prepopulated_fields = {'slug': ('blog_title',)}

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(BlogComment)