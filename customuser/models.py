from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    timestamp= models.DateTimeField(auto_now_add = True)


