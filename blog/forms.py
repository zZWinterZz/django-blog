"""Forms for blog app."""
from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    """Form for submitting comments."""
    class Meta:
        model = Comment
        fields = ('body',)

