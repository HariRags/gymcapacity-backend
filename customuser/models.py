from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    timestamp= models.DateTimeField(default=timezone.now)


