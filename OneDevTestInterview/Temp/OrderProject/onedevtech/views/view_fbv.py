import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from onedevtech.models import Profile, Order 
from onedevtech.serializers import OrderSerializer, ProfileSerializer
from onedevtech.permissions import OrderPermissions

@api_view(['GET', 'POST'])
@permission_classes([OrderPermissions])
def orders(request):
    if request.method == 'GET':
        order = Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# def profile_view():