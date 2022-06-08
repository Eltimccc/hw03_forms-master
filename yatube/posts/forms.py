from django.forms import ModelForm, Select, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']

        widgets = {
            "text": Textarea(attrs={
                'class':'form-control',
                'placeholder': 'Введите текст статьи'
            }),
            "group": Select(attrs={
                'class':'form-control',
                'placeholder': 'Введите текст статьи',
            }),
        }
