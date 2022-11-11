from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from django.db import models
import string
import random


User = get_user_model()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
       return ''.join(random.choice(chars) for _ in range(size))



class UserCreationViewSet(ModelViewSet):
    serializer_class =  UserSerializer

    def get_serializer_context(self):
         username = id_generator()
         return {'username':username}

    def get_queryset(self):
         return User.objects.all()     
