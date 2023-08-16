from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class Logout(View):
    def get(self, request):
        logout(self.request)
        return redirect(reverse('index'))
