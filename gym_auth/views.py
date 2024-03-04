# gym_auth/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.create_user(username=username, password=password)
    user_profile = UserProfile.objects.create(user=user)

    serializer = UserProfileSerializer(user_profile)
   
    return render(request, 'login.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect('welcome')
    return Response({'error': 'Invalid credentials'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def welcome(request):
    user_profile = UserProfile.objects.get(user=request.user)
    serializer = UserProfileSerializer(user_profile)
    return Response({'message': f'Welcome, {serializer.data["user"]["username"]}!'})

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def welcome_view(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')
