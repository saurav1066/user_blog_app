from django.forms import ModelForm

from .models import Blog


class BlogCreation(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body', 'author']
