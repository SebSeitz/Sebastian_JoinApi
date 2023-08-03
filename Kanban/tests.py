from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Task

class TaskTestCase(APITestCase):
    def test_create_and_retrieve_task(self):
        url = reverse('task-list')
        data = {'title': 'Test task'}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task_id = response.json()['id']
        task = Task.objects.get(pk=task_id)
        self.assertEqual(task.title, 'Test task')
