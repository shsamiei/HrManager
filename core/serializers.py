from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import test



class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']




