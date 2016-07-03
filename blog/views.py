from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

from .models import BlogPost
from .forms import SuggestForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'newest_blog_posts'

    def get_queryset(self):
        return BlogPost.objects.filter(
            post_date__lte=timezone.now()
        ).order_by('-post_date')[:5]


class ArchiveView(generic.ListView):
    template_name = 'blog/archive.html'
    context_object_name = 'archive_posts'
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.order_by('-post_date')


class BlogPostView(generic.DetailView):
    template_name = 'blog/post.html'
    model = BlogPost


class SuggestView(generic.FormView):
    template_name = 'blog/suggest.html'
    form_class = SuggestForm

    def get_success_url(self):
        messages.success(self.request, 'Suggestion submitted successfully!')
        return redirect('blog:blog_suggest')

    def form_valid(self, form):
        suggested = form.save(commit=False)
        suggested.topic_author = User.objects.get(id=self.request.user.id)
        suggested.save()
        return super(SuggestView, self).form_valid(form)
