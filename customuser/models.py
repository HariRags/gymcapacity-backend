from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):    #creating abstract user so as to add timestamp field to built in user model
    timestamp= models.DateTimeField(auto_now_add = True)


