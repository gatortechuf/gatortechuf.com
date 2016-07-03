from django import forms

from .models import BlogComment, SuggestedPost

class CommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment_author', 'comment_text', 'blog_post']


class SuggestForm(forms.ModelForm):

    class Meta:
        model = SuggestedPost
        fields = ['topic_idea']
