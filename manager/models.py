from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings



class Role(models.Model):

    SIMPLE_EMPLOYEE = "0"
    HR_MANAGER = "1"
    PAY_ROLL_MANAGER = "2"

    ROLE_CHOICES = [ 
        (SIMPLE_EMPLOYEE, ("Simple Employee")),
        (HR_MANAGER, ("Hr Manager")),
        (PAY_ROLL_MANAGER, ("Payroll Manager")),]
    
    title = models.CharField(max_length=1, choices = ROLE_CHOICES)

    class Meta:  
        ordering = ["title"]

    def __str__(self):
        return self.title



class EmployeeProfile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    role = models.ForeignKey(Role, blank=True, default=None, null=True, on_delete=models.SET_NULL)
    birth_date = models.DateField(blank=True, default=None, null=True)
    national_id = models.CharField(max_length=10, unique=True)


class Salary(models.Model):
    pass



