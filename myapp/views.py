# myapp/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Profile
from .serializer import StudentSerializer
from .models import Student
from .serializer import StudentSerializer1
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST','GET'])
def userapilogin(request, format=None):
    if request.method== 'GET':
        student= Profile.objects.all() #get all the drinks
        serializer= StudentSerializer(student, many=True)  #serialize them
        return Response(serializer.data)
    if request.method== 'POST':
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE'])
def userlist(request, format=None):
    if request.method=='GET':
        student= Profile.objects.all()
        serializer= StudentSerializer(student, many=True)
        return Response(serializer.data)
    if request.method=='DELETE':
        student= Profile.objects.get(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
            form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('welcome')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})

def welcome(request):
    return render(request, 'registration/welcome.html')

#below 2 are for testing purposes
@api_view(['POST', 'GET'])
def student_login(request, format=None):
    if request.method=='POST':
        serializer= StudentSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    if request.method=='GET':
        student= Student.objects.all()
        serializer= StudentSerializer1(student, many=True)
        return Response(serializer.data)

@api_view(['GET','DELETE'])
def student_list(request, format=None):
    if request.method=='GET':
        student= Student.objects.all()
        serializer= StudentSerializer1(student, many=True)
        return Response(serializer.data)
    if request.method=='DELETE':
        student= Student.objects.get(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)