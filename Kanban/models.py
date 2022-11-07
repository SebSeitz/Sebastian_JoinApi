from django.db import models
import datetime

class Category(models.Model):
    management = models.CharField(max_length=30)
    sales = models.CharField(max_length=30)
    marketing = models.CharField(max_length=30)
    product = models.CharField(max_length=30)

class Tasks(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    due_date = models.DateField(default=datetime.date.today)
    category = models.ForeignKey(Category)


