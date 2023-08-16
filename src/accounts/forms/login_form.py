from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Seu username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ex.: JohnDoe'
        })
    )
    password = forms.CharField(
        label='Sua senha',
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
