from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer, MyUserSerializer
from .models import Task, MyUser
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

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return HttpResponse(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = []





