from django.views import View
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from tasks.models import Task


@method_decorator(login_required, name='dispatch')
class TaskDelete(View):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.delete()
        return JsonResponse({'success': True})
