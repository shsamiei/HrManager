from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings



class BaseEmployee(models.Model):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    national_number = models.IntegerField()
    salary = models.IntegerField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


    



