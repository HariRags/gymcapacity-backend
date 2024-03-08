# gym_app/models.py
from django.db import models
from django.contrib.auth.models import User
from customuser.models import CustomUser    #custom user with timestamp field


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} {self.user.timestamp}"
