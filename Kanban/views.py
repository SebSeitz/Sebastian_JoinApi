from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer, MyUserSerializer, SubtaskSerializer
from .models import Task, MyUser, Subtask
from django.core import serializers
from django.http import HttpResponse
from datetime import datetime


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    permission_classes = []


    def create(self, request):
        users = request.data.get('users', [])
        due_date_str = request.data.get('due_date', '')
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None

        task = Task.objects.create(
            title=request.data.get('title', ''),
            description=request.data.get('description', ''),
            due_date=due_date,
            category=request.data.get('category', ''),
            status=request.data.get('status', ''),
        )
        task.user.set(users) # Many-to-Many-Feld setzen
        serialized_obj = serializers.serialize('json', [task,])
        return HttpResponse(serialized_obj, content_type='application/json')

class SubtaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subtasks to be viewed or edited.
    """
    queryset = Subtask.objects.all().order_by('completion_status')
    serializer_class = SubtaskSerializer
    permission_classes = []

    def create(self, request):
        task_id = request.data.get('task', '')  # Extract the task ID from the request data
        task = get_object_or_404(Task, id=task_id)  # Retrieve the associated task instance
        completion_status = request.data.get('completion_status', '').lower() == 'true'
        subtask = Subtask.objects.create(
            title=request.data.get('title', ''),
            description=request.data.get('description', ''),
            completion_status=completion_status,
             task=task,  # Set the associated task for the subtask
        )
        serializer = SubtaskSerializer(subtask)
        return HttpResponse(serializer.data, content_type='application/json')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = []







