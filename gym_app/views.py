from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Feedback
from .serializers import UserProfileSerializer, FeedbackSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from django.utils import timezone
from django.http import JsonResponse

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':    
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if user already exists
        user = User.objects.filter(username=username).first()

        if user is not None:
            # User already exists, authenticate
            user = authenticate(username=username, password=password)

            if user is not None:
                # If authentication is successful, update timestamp in UserProfile
                user.userprofile.timestamp = timezone.now()
                user.userprofile.save()

                
                return Response({"message": "Timestamp updated successfully"}, status=status.HTTP_200_OK)
            else:
                # If authentication fails, return error response
                return Response({"error": "Authentication failed check username and password"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # User does not exist, create new user and UserProfile
            user = User.objects.create_user(username=username, password=password)

            # Create UserProfile for the new user
            UserProfile.objects.create(user=user, timestamp=timezone.now())

            
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_view(request):
    users = User.objects.exclude(userprofile__timestamp__isnull=True)
    user_data = [{'username': user.username, 'id': user.id} for user in users]
    return Response(user_data)



@api_view(['DELETE'])
def delete_view(request, id):
    if request.method == 'DELETE':
        password = request.data.get('password')
        if not password:
            return Response({"error": "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if user.check_password(password):
            user.userprofile.timestamp = None
            user.userprofile.recently_deleted_timestamp = timezone.now() 
            user.userprofile.save()
            return Response({"message":"User deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def last_deleted_user_view(request):
    try:
        last_deleted_user_profile = UserProfile.objects.filter(recently_deleted_timestamp__isnull=False).latest('recently_deleted_timestamp')
        last_deleted_user = last_deleted_user_profile.user
        username = last_deleted_user.username
        return JsonResponse({'username': username}, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'No user has been deleted yet'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






