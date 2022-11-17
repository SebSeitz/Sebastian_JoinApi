
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Kanban.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
