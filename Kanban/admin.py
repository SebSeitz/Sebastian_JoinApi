from django.contrib import admin
from .models import Category, Tasks

admin.site.register(Category, Tasks)