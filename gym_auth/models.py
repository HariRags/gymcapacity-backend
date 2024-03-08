# gym_auth/models.py
from django.db import models
from django.contrib.auth.models import User
from customuser.models import CustomUser


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    