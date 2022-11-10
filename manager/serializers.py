from decimal import Decimal
from rest_framework import serializers
from .models import Role, EmployeeProfile, Salary
from django.db.models.aggregates import Count, Sum
from django.contrib.auth.models import User


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['title']

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['value', 'paid_time']
        

class EmployeeProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    role = RoleSerializer()
    salary = SalarySerializer()
    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'email', 'national_id', 'birth_date', 'role', 'salary']





