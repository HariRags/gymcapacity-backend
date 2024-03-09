# gym_app/models.py
from django.db import models
from django.contrib.auth.models import User
from customuser.models import CustomUser    #custom user with timestamp field


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} {self.user.timestamp}"

class Feedback(models.Model):                #creatinag a model to save feedback form database
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=20)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.timestamp}'