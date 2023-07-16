
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Kanban.views import TaskViewSet, UserViewSet, SubtaskViewSet, ContactsViewSet, LoginView, register
# from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)
router.register(r'subtasks', SubtaskViewSet)
router.register(r'contacts', ContactsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('register/', register, name='register'),
]
