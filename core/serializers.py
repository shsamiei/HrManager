from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


User = get_user_model()

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['email', 'password', 'username', 'first_name']



class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = ['email', 'first_name', 'last_name']


    def create(self, validated_data):
        username = self.context['username'] 
        return User.objects.create(username=username, **validated_data)

