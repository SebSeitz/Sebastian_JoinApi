from django.contrib import admin
from .models import Task, MyUser, Subtask

admin.site.register(Task)
admin.site.register(MyUser)
admin.site.register(Subtask)