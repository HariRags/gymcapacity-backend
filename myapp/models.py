# myapp/models.py
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username

#simple model created for testing stuff
class Student(models.Model):
    name= models.CharField(max_length=255)
    roll_no=models.CharField(max_length=7)
    timestamp= models.DateTimeField(auto_now_add = True )


    def __str__(self):
        return self.name + self.timestamp
