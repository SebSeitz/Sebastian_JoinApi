from django.contrib import admin
from .models import Task, MyUser, Subtask, Contacts

admin.site.register(Task)
admin.site.register(MyUser)
admin.site.register(Subtask)
admin.site.register(Contacts)