import json

from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import UserSerializer
from rest_framework import status


@api_view(['POST'])
def user_by_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            email = data['email']
            user = User.objects.get(email=email)
        except Exception as e:
            return Response({'Message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def sign_up_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'Message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
