from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название мема'
            }),
        }
