from decimal import Decimal
from rest_framework import serializers
from .models import Role, EmployeeProfile, Salary
from django.db.models.aggregates import Count, Sum
from django.contrib.auth import get_user_model


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['title']

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['value', 'paid_time']

# class SimpleEmployeeProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']


class PostEmployeeProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")

    def create(self, validated_data):
        user_id = self.context['user_id']
        user = get_user_model().objects.get(id=user_id)
        if EmployeeProfile.objects.filter(user_id=user_id): 
            raise serializers.ValidationError('The Employee is already Exist !')
        else : 
            user.first_name = validated_data['user'].pop('first_name')
            user.last_name = validated_data['user'].pop('last_name')
            user.email = validated_data['user'].pop('email')
            validated_data.pop('user')
            user.save()
            return EmployeeProfile.objects.create(user_id=user_id, **validated_data)


    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'email', 'national_id', 'birth_date', 'role', 'salary']


class GetEmployeeProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    role = RoleSerializer()
    salary = SalarySerializer()
    # user = SimpleEmployeeProfileSerializer()

    class Meta:
        model = EmployeeProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'national_id', 'birth_date', 'role', 'salary']

