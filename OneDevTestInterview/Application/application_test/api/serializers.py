from rest_framework import serializers
from .models import Application, Profile
from django.contrib.auth.models import User


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def create(self, validated_data):
        order = Application.objects.create(
            description=validated_data.get('description'),
            title = validated_data.get('title'),
            status = 'Sent',
            user = validated_data.get('user')
        )
        return order

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status')
        instance.save()
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Profile
        fields = ('id', 'email', 'image', 'birth_date', 'user')

    def create(self, validated_data):
        user = super(ProfileSerializer, self).create(validated_data)
        # user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email')
        instance.birth_date = validated_data.get('birth_date')
        instance.image = validated_data.get('image')
        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)