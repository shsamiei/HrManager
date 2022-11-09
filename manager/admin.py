from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models





@admin.register(models.BaseEmployee)
class BaseEmployeeAdmin(admin.ModelAdmin):
    list_display = ['phone', 'birth_date', 'national_number', 'salary']

