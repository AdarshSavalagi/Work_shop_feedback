from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager


class Students(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True, unique=True)
    phone = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    quiz = models.CharField(max_length=100, blank=True)
    feedback = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_created=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]

    def __str__(self):
        return self.usn
