"""Forms for about app."""
from django import forms
from about.models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """Form for submitting collaboration requests."""
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')