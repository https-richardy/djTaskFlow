from django.views import View
from django.shortcuts import (render, redirect)
from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.form import TaskForm
from tasks.models import Task
from django.urls import reverse


class TaskCreate(LoginRequiredMixin, View):
    template_name = 'tasks/task_create.html'
    login_url = 'accounts:login'

    def get(self, request):
        form = TaskForm()
        return render(self.request, self.template_name, {
            'form': form
        })

    def post(self, request):
        form = TaskForm(self.request.POST)
        if form.is_valid():
            task: Task = form.save(commit=False)
            task.user = self.request.user
            form.save()
            return redirect(reverse('tasks:list'))
        return render(self.request, self.template_name, {
            'form': form
        })
