from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        label='Escolha um username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: JohnDoe'
        })
    )
    password = forms.CharField(
        label='Escolha uma senha segura',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha'
        })
    )

    class Meta:
        model = User
        fields = (
            'username', 'password'
        )
