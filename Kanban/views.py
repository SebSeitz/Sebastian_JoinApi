from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import TaskSerializer, MyUserSerializer, SubtaskSerializer, ContactSerialzier
from .models import Task, MyUser, Subtask, Contacts
from django.core import serializers as core_serializers
from django.http import HttpResponse
from datetime import datetime
from .serializers import MyUserSerializer
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    permission_classes = []


    def create(self, request):
        users = request.data.get('users', [])
        subtask = request.data.get('subtask', [])
        due_date_str = request.data.get('due_date', '')
        due_date = datetime.strptime(due_date_str, '%Y-%m-%d').date() if due_date_str else None

        task = Task.objects.create(
            title=request.data.get('title', ''),
            description=request.data.get('description', ''),
            due_date=due_date,
            category=request.data.get('category', ''),
            urgency=request.data.get('urgency', ''),
            status=request.data.get('status', ''),
        )
        task.user.set(users) # Many-to-Many-Feld setzen
        task.subtasks.set(subtask)
        serialized_obj = core_serializers.serialize('json', [task,])
        return HttpResponse(serialized_obj, content_type='application/json', status=status.HTTP_201_CREATED)

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
        completion_status = str(request.data.get('completion_status', '')).lower() == 'true'
        subtask = Subtask.objects.create(
            title=request.data.get('title', ''),
            completion_status=completion_status,
            task=task,  # Set the associated task for the subtask
        )

        task.subtasks.add(subtask)
        task.save()
        serializer = SubtaskSerializer(subtask)
        return HttpResponse(serializer.data, content_type='application/json', status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = []



class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all().order_by('user')
    serializer_class = ContactSerialzier
    permission_classes = []


    def create(self, request):
        user_id = request.data.get('user')
        user = get_object_or_404(MyUser, id=user_id)
        contact = Contacts.objects.create(
            user = user,
            email=request.data.get('email', ''),
            first_name=request.data.get('first_name', ''),
            last_name=request.data.get('last_name', ''),

        )
        user.myContacts.add(contact)  # Assign the contact to the user's myContacts fiel
        user.save()
        serializer = ContactSerialzier(contact)
        return HttpResponse(serializer.data, content_type='application/json')

class LoginView(ObtainAuthToken):
     def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

@api_view(['POST'])
def register(request):
    VALID_USER_FIELDS = [f.name for f in MyUser._meta.fields]
    DEFAULTS = {
        # you can define any defaults that you would like for the user here
    }

    serialized = MyUserSerializer(data=request.data)

    if serialized.is_valid():
        user_data = {field: data for (field, data) in request.data.items() if field in VALID_USER_FIELDS}
        user_data.update(DEFAULTS)

        # Hash the password before creating the user
        password = request.data.get('password')
        hashed_password = make_password(password)
        user_data['password'] = hashed_password

        # Create the user with the hashed password
        user = MyUser(**user_data)
        user.set_password(password)
        user.save()
        return Response(MyUserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)








