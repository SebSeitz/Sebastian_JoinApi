from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TaskSerializer, MyUserSerializer
from .models import Task, MyUser
from django.core import serializers
from django.http import HttpResponse

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    permission_classes = []

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = []


    def create(self, request):
        task = Task.objects.create(title= request.POST.get('title', ''),
                                  description= request.POST.get('description', ''),
                                  due_date = request.POST.get('due_date', ''),
                                  category = request.POST.get('category', ''),
                                  user= request.user
                                )

        user = MyUser.objects.create(first_name = request.get('first_name', ''))
        serialized_obj = serializers.serialize('json', [task, user ])
        return HttpResponse(serialized_obj, content_type='application/json')


