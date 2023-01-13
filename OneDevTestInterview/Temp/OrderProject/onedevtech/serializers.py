from rest_framework import serializers
from onedevtech.models import Profile, Order
from django.contrib.auth.models import User

class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    is_staff = serializers.BooleanField(default=False, read_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=255)
    image = serializers.CharField(max_length=10000)
    date_of_birth = serializers.DateTimeField(read_only=True, format='%d.%m.%Y')

    class Meta:
        model = User
        fields = ('id', 'password', 'is_staff', 'email', 'first_name', 'last_name', 'date_of_birth', 'image')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'name', 'description', 'user_id']
