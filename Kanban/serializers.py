from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, MyUser, Subtask

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


class SubtaskSerializer(serializers.ModelSerializer):
     task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

     class Meta:
        model = Subtask
        fields = ['id', 'title', 'completion_status', 'task']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=MyUser.objects.all())
    subtasks = SubtaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'urgency', 'category', 'status', 'user', 'subtasks']




