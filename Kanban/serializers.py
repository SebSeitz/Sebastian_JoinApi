from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, MyUser

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = MyUserSerializer()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'category', 'user']