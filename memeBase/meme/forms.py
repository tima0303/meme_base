from .models import Meme

from django.forms import ModelForm, TextInput, Textarea


class MemeForm(ModelForm):
    class Meta:
        model = Meme
        fields = ['title', 'content', 'photo', 'tags']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название мема'
            }),
            "content": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание мема'
            }),
            "tags": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название тега'
            }),


        }

