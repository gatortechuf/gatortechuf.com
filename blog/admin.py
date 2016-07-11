from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import BlogPost, SuggestedPost

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'blog_author')
    search_fields = ('blog_title', 'blog_content')
    prepopulated_fields = {'slug': ('blog_title',)}
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget}
    }
    fieldsets = [
        ('Title and URL', {'fields': ('blog_title', 'slug')}),
        ('Blog Content', {'fields': [('blog_content')]})
    ]

    def save_model(self, request, obj, form, change):
        obj.blog_author = request.user
        obj.save()


class SuggestAdmin(admin.ModelAdmin):
    list_display = ('topic_date', 'topic_author', 'topic_idea')

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(SuggestedPost, SuggestAdmin)
