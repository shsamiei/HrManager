from decimal import Decimal
from rest_framework import serializers
from .models import Role, EmployeeProfile
from django.db.models.aggregates import Count, Sum


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['title']


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ['role', 'national_id', 'birth_date']

