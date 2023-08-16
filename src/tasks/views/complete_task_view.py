from django.views import View
from django.shortcuts import get_object_or_404

from django.http import JsonResponse
from tasks.models import Task


class TaskComplete(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.completed = True
        task.save()
        return JsonResponse({"success": True})
