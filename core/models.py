from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20)
    real_user = models.BooleanField(default=True)
    department=models.CharField(max_length=50,blank=True)
    feedback = models.JSONField(blank=True, null=True)
    quiz = models.JSONField(blank=True,null=True)
    quiz_marks = models.IntegerField(default=0)

    def has_attended_quiz(self):
        return 'Yes' if self.quiz is not None else 'No'

    def __str__(self):
        return self.username