from django.views import View
from django.shortcuts import render, redirect
from accounts.forms import SignupForm


class Signup(View):
    template_name = 'accounts/signup.html'

    def get(self, request):
        form = SignupForm()
        return render(self.request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = SignupForm(self.request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')

            user.set_password(password)
            user.save()
            return redirect('accounts:login')

        return render(self.request, self.template_name, {
            'form': form
        })
