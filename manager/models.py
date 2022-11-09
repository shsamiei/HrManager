from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# class Salary(models.Model):
#     value = models.IntegerField()
#     paid_date = models.DateField(auto_now_add=True)


class BaseEmployee(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    national_number = models.IntegerField()
    salary = models.IntegerField()


    

class Employee(BaseEmployee):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class HrManager(BaseEmployee):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class PayRollManager(BaseEmployee):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name



