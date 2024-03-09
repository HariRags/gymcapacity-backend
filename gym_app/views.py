# gym_app/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from django.shortcuts import render, redirect,get_object_or_404 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import get_user_model
from .models import Feedback
from django.utils import timezone


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get('username') #get username&password
    password = request.data.get('password')
    User = get_user_model()

    user = authenticate(request, username=username, password=password) #check if user exists in database or not
    if user is not None:
         user.timestamp=timezone.now   #update new login time
         return redirect('welcome')    #if user exists then directly redirect
    else:
        user = User.objects.create_user(username=username, password=password)  #if user does not exist in database then create that user
        user_profile = UserProfile.objects.create(user=user)
        serializer = UserProfileSerializer(user_profile)
        return redirect('welcome')

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

def home_view(request):
    return render(request,'main.html')

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


def welcome_view(request):
    
        user = get_user_model()  #get all users
        if user.timestamp is not None:   #check if timestamp is not null
            mymembers =user.objects.filter().values()
        template = loader.get_template('welcome.html')
        context = {                                        #pass users to the html page to display the list
                  'mymembers': mymembers,
                 }
        return HttpResponse(template.render(context, request))
    

def exit_view(request): #this is to show delete buttons in the memebers list
        user = get_user_model()      #get all users
        if user.timestamp is not None:        #check if timestamp is not null
            mymembers =user.objects.filter().values()
        template = loader.get_template('exit.html')
        context = {                                        #pass users to the html page to display the list
                  'mymembers': mymembers,
                 }
        return HttpResponse(template.render(context, request))

def deletes(request, id): #this is to delete a particular member
    user = get_user_model()
    mymembers =user.objects.get(id=id)     
    template = loader.get_template('delete.html')
    context = {
                  'mymembers': mymembers,
                 }
    if request.method == 'POST':    #get password
        password = request.POST.get('password')
        User = authenticate(username=mymembers.username, password=password)   #check if the password matches
        if User is not None:
            # Password is correct, delete the user
            User.timestamp= None
            return redirect('home')
        else:                    #if it doesnt match then redirect to the list
            return redirect('welcome')
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    return redirect('login')



def feedback(request):                   #creating object basically row with data name roll and description as column
    if request.method == 'POST':
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        description = request.POST.get('description')

         # Save the feedback to the database
        feedback_obj = Feedback.objects.create(name=name, roll=roll, description=description)

        # Pass feedback details to the success page
        return redirect('success', feedback_id=feedback_obj.id)

   

def success(request, feedback_id): #get_object_or_404 is a shortcut function that retrieves an object from the database or raises a 404 error if the object is not found.  
    feedback_obj = get_object_or_404(Feedback, id=feedback_id)
    return render(request, 'success.html', {'feedback': feedback_obj})




