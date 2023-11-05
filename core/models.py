from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.
class Students(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    

