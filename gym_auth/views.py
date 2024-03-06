# gym_auth/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model


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
        user = get_user_model()
        mymembers =user.objects.all().values()
        template = loader.get_template('welcome.html')
        context = {
                  'mymembers': mymembers,
                 }
        return HttpResponse(template.render(context, request))
    return redirect('login')

def exit_view(request):
    if request.user.is_authenticated:
        user = get_user_model()
        mymembers =user.objects.all().values()
        template = loader.get_template('exit.html')
        context = {
                  'mymembers': mymembers,
                 }
        return HttpResponse(template.render(context, request))
    return render(request, 'exit.html')

def details(request, id):
    user = get_user_model()
    mymembers =user.objects.get(id=id)
    template = loader.get_template('delete.html')
    context = {
                  'mymembers': mymembers,
                 }
    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user is not None:
            # Password is correct, delete the user
            user.delete()
            return redirect('login')
        else:
            return redirect('welcome')

    return HttpResponse(template.render(context, request))
    



def logout_view(request):
    logout(request)
    return redirect('login')
