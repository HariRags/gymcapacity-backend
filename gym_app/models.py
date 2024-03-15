from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, blank=False,unique=True) 
    password = models.CharField(max_length=128, blank=False)

    def __str__(self):
        return self.username

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=20)
    description = models.TextField()
    feedback_type = models.CharField(max_length=20, choices=[('suggestion', 'Suggestion'), ('complaint', 'Complaint')], default='suggestion')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.timestamp}'