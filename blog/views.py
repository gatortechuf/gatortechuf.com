from django.views import generic
from django.utils import timezone
from django.core.urlresolvers import reverse

from .models import BlogPost, BlogComment
from .forms import CommentForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'newest_blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')[:10]


class BlogPostView(generic.DetailView):
    template_name = 'blog/post.html'
    form_class = CommentForm
    model = BlogPost

class CommentView(generic.FormView):
    template_name = 'blog/form.html'
    form_class = CommentForm
    model = BlogComment
    # This needs to return the user to the blog post they were on
    success_url = '/blog/'

    # This needs to actually validate the form data
    def form_valid(self, form):
        form.save(commit = True)
        return super(CommentView, self).form_valid(form)
