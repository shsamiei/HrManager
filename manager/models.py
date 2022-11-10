from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .enums import RollChoices

class Role(models.Model):
    title = models.CharField(max_length=64 ,choices=RollChoices.choices)

    class Meta:  
        ordering = ["title"]

    def __str__(self):
        return self.title


class EmployeeProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    role = models.ForeignKey(Role, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    birth_date = models.DateField(blank=True, default=None, null=True)
    national_id = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.user.first_name


class Salary(models.Model):
    value = models.PositiveIntegerField(default=0)
    paid_time = models.DateField(auto_now_add=True)
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE, related_name='salary')
    
    def __str__(self):
        return str(self.value)













