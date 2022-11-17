from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import User



class Category(models.Model):
    CATEGORY_CHOICES = [
        ('MT','MANAGEMENT'),
        ('SL', 'SALES'),
        ('MK','MARKETING'),
        ('PR','PRODUCT'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='MT')

class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    due_date = models.DateField(default=datetime.date.today)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )


