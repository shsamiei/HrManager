
from django.db import models


class RollChoices(models.TextChoices):
    SIMPLE_EMPLOYEE = 'simple_employee'
    HR_MANAGER =  'hr_manager'
    PAY_ROLL_MANAGER = 'payroll_manager'

