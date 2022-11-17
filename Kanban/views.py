from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    permission_classes = []
