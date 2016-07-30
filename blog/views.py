from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils import timezone
from django.views import generic

from .forms import SuggestForm, CommentForm
from .models import BlogPost


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


class CommentView(generic.FormView):
    template_name = 'blog/comment.html'
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.comment_author = User.objects.get(id=self.request.user.id)
        comment.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


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
