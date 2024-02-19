from rest_framework import serializers
from .models import Profile, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Profile
        fields=['username','password','timestamp']

class StudentSerializer1(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=['id','name','roll_no','timestamp']