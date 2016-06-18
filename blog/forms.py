from django import forms

from .models import BlogComment

class CommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment_author', 'comment_text', 'blog_post']
