from rest_framework.permissions import BasePermission
from .models import Role, Salary, EmployeeProfile
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


User = get_user_model()

class IsHrManager(BasePermission):
    
    def has_permission(self, request, view):
        employee = EmployeeProfile.objects.get(user_id=request.user.id)
        if employee.role.title == 'hr_manager':
            return True 
        return False


class IsPayRollManager(BasePermission):
    def has_permission(self, request, view):
        employee = EmployeeProfile.objects.get(user_id=request.user.id)
        if employee.role.title == 'payroll_manager':
            return True 
        return False
        

class IsHrOrPayRollManager(BasePermission):
    def has_permission(self, request, view):
        employee = EmployeeProfile.objects.get(user_id=request.user.id)
        if employee.role.title != 'simple_employee' :
            print(employee.role.title )

            return True 
        return False

