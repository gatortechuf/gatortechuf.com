from django import forms

from .models import SuggestedPost


class SuggestForm(forms.ModelForm):

    class Meta:
        model = SuggestedPost
        fields = ['topic_idea']
