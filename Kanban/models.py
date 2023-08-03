from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save



class Contacts(models.Model):
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)

class Subtask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name="subtasks_set")
    title = models.CharField(max_length=30)
    completion_status = models.BooleanField(default=True)


class Task(models.Model):

  CATEGORY_CHOICES = [
  ('Management','MANAGEMENT'),
  ('Sales', 'SALES'),
  ('Marketing','MARKETING'),
  ('Product','PRODUCT'),
]
  URGENCY_CHOICES = [
  ('High','HIGH'),
  ('Mid', 'MEDIUM'),
  ('Low','LOW'),

]
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=100)
  due_date = models.DateField(default=datetime.date.today)
  urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='High')
  category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='Management')
  status = models.CharField(max_length=15, default='todo')
  user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )
  subtasks = models.ManyToManyField(Subtask, related_name="tasks", blank=True)


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)



class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    password = models.CharField(('password'), max_length=40, blank=True)
    myContacts = models.ManyToManyField(Contacts, related_name='users', blank=True)
    is_active = models.BooleanField(('active'), default=True)
    is_staff = models.BooleanField(('staff status'), default=False)
    is_superuser = models.BooleanField(('superuser status'), default=False)
    date_joined = models.DateTimeField(('date joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()


    def has_module_perms(self, app_label):
        """
        Does the user have permissions to view the app `app_label`?
        """
        return True





