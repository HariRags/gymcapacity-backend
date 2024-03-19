from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    recently_deleted_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Feedback(models.Model):
    name = models.CharField(max_length=255,)
    roll = models.CharField(max_length=20,)
    description = models.TextField()
    feedback_type = models.CharField(max_length=20, choices=[('suggestion', 'Suggestion'), ('complaint', 'Complaint'),('appreciation','Appreciation'),('others','Others')], default='suggestion')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.timestamp}'
