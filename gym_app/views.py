from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Feedback
from .serializers import UserProfileSerializer, FeedbackSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import status

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':    
        username = request.data.get('username') #get username&password
        password = request.data.get('password')
        User = get_user_model()

        user = authenticate(request, username=username, password=password) #check if user exists in database or not
        if user is not None:
            user_profile=user
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            user = User.objects.create_user(username=username, password=password,is_staff=True, is_superuser=True)  #if user does not exist in database then create that user
            user_profile = UserProfile.objects.create(user=user)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def list_view(request):
    user=get_user_model()
    users = user.objects.all()
    # Create a list of dictionaries containing only usernames
    usernames = [{'username': user.username} for user in users]
    return Response(usernames)

@api_view(['DELETE'])
def delete_view(request, id):
    if request.method =='DELETE':
        password=request.data.get('password')   #get password
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user=get_user_model()
            mymember=user.objects.get(id=id)
            User=authenticate(username=mymember.username, password=password)
            if User is not None:
                User.delete()   #if password is correct delete the user
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        except user.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
