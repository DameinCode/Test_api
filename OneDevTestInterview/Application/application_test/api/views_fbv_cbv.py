import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView

from django.contrib.auth.models import User
from api.models import Application, Profile
from api.serializers import OrderSerializers, ProfileSerializer, UserSerializer
from api.permissions import OrderPermissions, OrderToPuPermissions, ProfilePermissions


class OrderList(APIView):
    for_null_users = 0
    permission_classes = [OrderPermissions]
    def get(self, request):
        if(request.user.is_authenticated == False):
            orders = Application.objects.filter(user=None)
            print(orders)
        else:
            orders = Application.objects.filter(user=request.user)
        serializer = OrderSerializers(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.user)
        request.data["user"] = request.user.id
        serializer = OrderSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profileview(APIView):
    permission_classes = [ProfilePermissions]

    def get(self, request):
        profiles = Profile.objects.filter(user=request.user)
        # print()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def put(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
            user = User.objects.get(username=request.user.username)
        except Exception as e:
            return Response({'Message': str(e)})
        user_data = {
            "username": request.data["email"]
        }
        user_serializer = UserSerializer(instance = user, data = user_data)
        serializer = ProfileSerializer(instance = profile, data = request.data)
        if(user_serializer.is_valid()):
            user_serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([OrderToPuPermissions])
def order_detail(request, order_id):
    try:
        order = Application.objects.get(id=order_id)
    except Exception as e:
        return Response({'Message': str(e)})
    if request.method == 'PUT':
        serializer = OrderSerializers(instance=order, data = request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        if request.method == 'GET':
            serializer = OrderSerializers(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
