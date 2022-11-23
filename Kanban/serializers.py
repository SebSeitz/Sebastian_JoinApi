from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'category', 'user']