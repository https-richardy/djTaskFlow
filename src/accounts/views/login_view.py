from django.views import View
from django.shortcuts import (render, redirect)
from django.contrib import messages

from django.contrib.auth import (authenticate, login)
from accounts.forms import LoginForm


class Login(View):
    template_name = 'accounts/login.html'

    def get(self, request):
        form = LoginForm()
        return render(self.request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(self.request, username=username,
                                password=password)
            if user is not None:
                login(self.request, user)
                return redirect('tasks:list')
            else:
                messages.error(self.request, 'E-mail ou senha inválidos.')
                return render(self.request, self.template_name, {
                    'form': form
                })

        return render(self.request, self.template_name, {
            'form': form
        })
