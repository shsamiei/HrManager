from django.db import models


class Salary(models.Model):
    value = models.IntegerField()
    paid_date = models.DateField(auto_now_add=True)


class BaseEmployee(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    national_number = models.IntegerField()
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)
    
    

class Employee(BaseEmployee):
    pass

class HrManager(BaseEmployee):
    pass

class PayRollManager(BaseEmployee):
    pass


