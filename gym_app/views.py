from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserProfile, Feedback
from .serializers import UserProfileSerializer, FeedbackSerializer

@api_view(['POST'])
def register_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    UserProfile.objects.create(username=username, password=password)
    
    return Response({'message': 'Registration successful'})

@api_view(['GET'])
def list_view(request):
    users = UserProfile.objects.all()
    # Create a list of dictionaries containing only usernames
    usernames = [{'username': user.username} for user in users]
    return Response(usernames)

@api_view(['DELETE'])
def delete_view(request, username):
    password = request.data.get('password')
    try:
        user = UserProfile.objects.get(username=username)
    except UserProfile.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)

    if user.password != password:
        return Response({'message': 'Incorrect password'}, status=400)

    user.delete()
    return Response({'message': 'User deleted successfully'})

@api_view(['POST'])
def feedback_view(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
