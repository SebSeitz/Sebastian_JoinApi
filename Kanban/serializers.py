from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Task, MyUser, Subtask, Contacts


class ContactSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['id', 'email', 'first_name', 'last_name', 'user']

class MyUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'myContacts']

class SubtaskSerializer(serializers.ModelSerializer):
     task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

     class Meta:
        model = Subtask
        fields = ['id', 'title', 'completion_status', 'task']

class SubtaskIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(many=True, queryset=MyUser.objects.all())
    subtasks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='id')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'urgency', 'category', 'status', 'user', 'subtasks']




