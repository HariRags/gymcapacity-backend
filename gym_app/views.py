from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Feedback
from .serializers import UserProfileSerializer, FeedbackSerializer
from django.contrib.auth.models import User
from rest_framework import status

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':    
        username = request.data.get('username')
        password = request.data.get('password')

        user, created = User.objects.get_or_create(username=username)
        if created:
            user.set_password(password)
            user.save()
            user_profile = UserProfile.objects.create(user=user)
            serializer = UserProfileSerializer(user_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

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
            user.userprofile.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
