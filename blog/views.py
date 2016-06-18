from django.views import generic
from django.utils import timezone

from .models import BlogPost


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'newest_blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')[:10]


class BlogPostView(generic.DetailView):
    template_name = 'blog/post.html'
    model = BlogPost
