from django.db import models


class BaseEmployee(models.Model):
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    national_number = models.IntegerField()
    

