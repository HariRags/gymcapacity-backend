from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Feedback
from .serializers import UserProfileSerializer, FeedbackSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework import status
from django.utils import timezone


@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':    
        username = request.data.get('username') #get username&password
        password = request.data.get('password')
        User = get_user_model()

        user = authenticate(request, username=username, password=password) #check if user exists in database or not
        if user is not None:
            user_profile=user
            user.timestamp=timezone.now()
            user.save()
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            user = User.objects.create_user(username=username, password=password,is_staff=True, is_superuser=True)  #if user does not exist in database then create that user
            user_profile = UserProfile.objects.create(user=user)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def list_view(request):
    user_model = get_user_model()
    users = user_model.objects.exclude(timestamp__isnull=True)  # Exclude users with timestamp=None
    user_data = [{'username': user.username, 'id': user.id} for user in users]
    return Response(user_data)


@api_view(['DELETE'])
def delete_view(request, id):
    if request.method == 'DELETE':
        password = request.data.get('password')   # Get password from request data
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            User = get_user_model().objects.get(id=id)
        except get_user_model().DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        # Authenticate user
        authenticated_user = authenticate(username=User.username, password=password)
        
        if authenticated_user is not None:
            # Password is correct, update timestamp and save
            authenticated_user.timestamp = None
            authenticated_user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            # Invalid credentials
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
