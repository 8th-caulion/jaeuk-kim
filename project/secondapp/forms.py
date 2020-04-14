from django import forms
from .models import Blog
 
class Write(forms.ModelForm):
    class Meta:
        model = Blog
 
        fields = ['title', 'author', 'body'] 