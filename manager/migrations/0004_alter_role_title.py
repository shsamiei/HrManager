# Generated by Django 4.1.3 on 2022-11-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_salary_alter_employeeprofile_national_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='title',
            field=models.CharField(choices=[('simple_employee', '0'), ('1', 'hr_manager'), ('2', 'payroll_manager')], max_length=64),
        ),
    ]
