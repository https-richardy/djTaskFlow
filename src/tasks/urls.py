from django.urls import path
from tasks.views import (
    TaskCreate, TaskList,
    TaskDelete, TaskComplete
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('complete/<int:pk>/', TaskComplete.as_view(), name='complete')
]
