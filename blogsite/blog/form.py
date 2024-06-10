from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control name-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control description-input'}),
        }
