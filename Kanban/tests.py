from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
import json
from .models import Task, MyUser
from datetime import datetime

class TaskTestCase(APITestCase):
    def test_create_and_retrieve_task(self):
        url = reverse('task-list')
        data = {'title': 'Test task',
                'due_date': '2012-04-23'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = json.loads(response.content.decode('utf-8'))  # Decode and parse JSON

        if isinstance(response_data, list):  # Check if the response_data is a list
            task_id = response_data[0]['pk']  # Assuming response_data is a list of dictionaries
        else:
            task_id = response_data['id']  # Use the original structure if it's not a list

        task = Task.objects.get(pk=task_id)
        self.assertEqual(task.title, 'Test task')

class UserRegistrationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_user_registration(self):
        user_data = {
            'email': 'longsillytestemail@example.com',
            'password': 'testpassword123456',
            'first_name': 'Test',
            'last_name': 'User',
        }

        response = self.client.post('/register/', user_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], user_data['email'])
        self.assertEqual(response.data['first_name'], user_data['first_name'])
        self.assertEqual(response.data['last_name'], user_data['last_name'])


        self.assertEqual(MyUser.objects.count(), 1)
        user = MyUser.objects.get(email=user_data['email'])
        self.assertTrue(user.check_password(user_data['password']))


class TaskAssignmentTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_assign_multiple_users_to_task(self):
        # Create two user instances for testing
        user1 = MyUser.objects.create(email='user1@example.com', password='password1')
        user2 = MyUser.objects.create(email='user2@example.com', password='password2')

        # Define the task data with assigned users and a valid due_date
        task_data = {
            'title': 'Test Task',
            'description': 'This is a test task.',
            'users': [user1.id, user2.id],  # Assign both users to the task
            'due_date': datetime.now().date(),  
            'status': 'todo',
        }

        url = reverse('task-list')
        response = self.client.post(url, task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response_data = json.loads(response.content.decode('utf-8'))
        task_id = response_data[0]['pk']

        task = Task.objects.get(pk=task_id)

        self.assertEqual(task.title, task_data['title'])
        self.assertEqual(task.description, task_data['description'])

        self.assertEqual(task.user.count(), 2)
        self.assertIn(user1, task.user.all())
        self.assertIn(user2, task.user.all())