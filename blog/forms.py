from django import forms

from .models import BlogComment, SuggestedPost


class SuggestForm(forms.ModelForm):

    class Meta:
        model = SuggestedPost
        fields = ['topic_idea']


class CommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment_content', 'comment_blog_post']