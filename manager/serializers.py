from rest_framework import serializers
from .models import Role, EmployeeProfile, Salary
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password




class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['title']


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Salary
        fields = ['value', 'paid_time']

    def create(self, validated_data):
        employee_id = self.context['employee_id']
        return Salary.objects.create(employee_id=employee_id, **validated_data)




class PostEmployeeProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    username = serializers.CharField(source="user.username")
    password = serializers.CharField(source="user.password")
    
    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return make_password(value)

    def create(self, validated_data):
        user_id = self.context['user_id']
        user = get_user_model().objects.get(id=user_id)

        if EmployeeProfile.objects.filter(user_id=user_id): 
            raise serializers.ValidationError('The Employee is already Exist !')

        else : 
            user.first_name = validated_data['user'].pop('first_name')
            user.last_name = validated_data['user'].pop('last_name')
            user.email = validated_data['user'].pop('email')
            user.username = validated_data['user'].pop('username')
            user.password = validated_data['user'].pop('password')
            validated_data.pop('user')
            user.save()
            
            return EmployeeProfile.objects.create(user_id=user_id, **validated_data)


    class Meta:
        model = EmployeeProfile
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'national_id', 'birth_date', 'role']


class GetEmployeeProfileSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    role = RoleSerializer(read_only=True)
    salary = SalarySerializer(many=True, read_only=True)


    def validate_national_id(self, value):
        if len(value) != 10 : 
            raise serializers.ValidationError("national_id should be equal 10 digits")
        return value


    def update(self, instance, validated_data):

        user_id = self.context['user_id']
        user = get_user_model().objects.get(id=user_id)

        user.first_name = validated_data.get('user').get('first_name')
        user.last_name = validated_data.get('user').get('last_name')
        user.email = validated_data.get('user').get('email')
        user.save()
        
        instance.national_id = validated_data.get('national_id')
        instance.birth_date = validated_data.get('birth_date')
        instance.national_id = validated_data.get('national_id')

        instance.save()
        return instance

    class Meta:
        model = EmployeeProfile
        fields = ['id','first_name', 'last_name', 'email', 'national_id', 'birth_date', 'role', 'salary']
        read_only_fields = ['salary']





