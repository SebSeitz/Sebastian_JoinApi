from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, MyUser, Subtask

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    # user = MyUserSerializer()
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=MyUser.objects.all())
    subtask = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'urgency', 'category', 'status', 'user', 'subtask']

class SubtaskSerializer(serializers.ModelSerializer):
     task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

     class Meta:
        model = Subtask
        fields = ['title', 'description', 'completion_status', 'task']


