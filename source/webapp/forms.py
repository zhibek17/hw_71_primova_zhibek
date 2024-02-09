from django import forms
from .models import Publication


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ['picture', 'description']