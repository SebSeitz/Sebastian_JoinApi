from django.db import models
import datetime
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _



class Task(models.Model):

  CATEGORY_CHOICES = [
  ('MT','MANAGEMENT'),
  ('SL', 'SALES'),
  ('MK','MARKETING'),
  ('PR','PRODUCT'),
]
  URGENCY_CHOICES = [
  ('H','HIGH'),
  ('M', 'MEDIUM'),
  ('L','LOW'),

]
  title = models.CharField(max_length=30)
  description = models.CharField(max_length=30)
  due_date = models.DateField(default=datetime.date.today)
  urgency = models.CharField(max_length=2, choices=URGENCY_CHOICES, default='H')
  category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='MT')
  user = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )

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
        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(('email address'), unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
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