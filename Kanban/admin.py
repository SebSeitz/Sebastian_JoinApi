from django.contrib import admin
from .models import Task, MyUser

admin.site.register(Task)
admin.site.register(MyUser)