from django.db.models.aggregates import Count, Sum 
from django.db.models import Q, F
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response 
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin , RetrieveModelMixin , UpdateModelMixin
from .models import Role, EmployeeProfile
from .serializers import RoleSerializer, PostEmployeeProfileSerializer, GetEmployeeProfileSerializer

                         

class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class EmployeeProfileViewSet(ModelViewSet):
    queryset = EmployeeProfile.objects.all()


    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostEmployeeProfileSerializer
        return GetEmployeeProfileSerializer

    def get_serializer_context(self):
         return {'user_id': 8}

