from django.contrib import auth
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.serializers import Serializer
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, ProfileSerializer
from django.contrib.auth import get_user_model
from .models import Profile


@api_view(['GET'])
def userList(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def profileList(request):
    profiles = Profile.objects.all()
    serializer = ProfileSerializer(profiles, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def profileUpdate(request, user_id):
    bio = request.data['bio']
    picture = request.data['picture']
    profile = Profile.objects.get(user=user_id)
    profile.bio = bio
    profile.picture = picture
    profile.save()
    return Response({"message": "updated"})


@api_view(['GET'])
def searchUser(request, search):
    users = get_user_model().objects.all()
    if search != "":
        users = users.filter(username__icontains=search).order_by(
            'username')[:10]
        if len(users) < 1:
            return Response({"error": "User not found"})
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
