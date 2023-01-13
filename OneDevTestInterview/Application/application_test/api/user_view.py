import json

from django.contrib.auth.models import User

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from api.serializers import ProfileSerializer, UserSerializer
from rest_framework import status
from api.models import Profile


@api_view(['POST'])
def user_by_username(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            username = data['username']
            user = User.objects.get(username=username)
        except Exception as e:
            return Response({'Message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def sign_up_user(request):
    if request.method == 'POST':
        print(request.data)
        user_data = {
            # "username": request.data.username,
            "username": request.data["email"],
            "password": request.data["password"]
        }
        serializer = UserSerializer(data=user_data)
        if serializer.is_valid():
            serializer.save()
        request.data["user"] = serializer.data["id"]
        serializerProfile = ProfileSerializer(data=request.data)
        if serializerProfile.is_valid():
            serializerProfile.save()
            return Response(serializerProfile.data, status=status.HTTP_201_CREATED)
        return Response({'Message': serializerProfile.errors}, status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

