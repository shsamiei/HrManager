# Generated by Django 4.1.3 on 2022-11-12 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_employeeprofile_options_alter_role_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeprofile',
            options={},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='employeeprofile',
            name='role',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='manager.role'),
        ),
    ]
