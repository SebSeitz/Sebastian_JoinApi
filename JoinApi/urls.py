
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Kanban.views import TaskViewSet, UserViewSet
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
