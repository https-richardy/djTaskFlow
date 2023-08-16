from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from tasks.models import Task
from tasks.form import TaskForm


class TaskList(LoginRequiredMixin, View):
    template_name = 'tasks/task_list.html'
    login_url = 'accounts:login'

    def get(self, request):
        tasks = Task.objects.filter(user=self.request.user, completed=False)
        form = TaskForm()
        return render(self.request, self.template_name, {
            'tasks': tasks,
            'form': form
        })
