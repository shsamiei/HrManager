from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

User = get_user_model()


# @api_view(['GET', 'POST'])
# @permission_classes((AllowAny,))
# def user_creation(request):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserCreationViewSet(ModelViewSet):
    serializer_class =  UserSerializer

    def get_queryset(self):
         return User.objects.all()     
