# Generated by Django 4.1.3 on 2022-11-09 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('national_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('paid_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('baseemployee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manager.baseemployee')),
            ],
            bases=('manager.baseemployee',),
        ),
        migrations.CreateModel(
            name='HrManager',
            fields=[
                ('baseemployee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manager.baseemployee')),
            ],
            bases=('manager.baseemployee',),
        ),
        migrations.CreateModel(
            name='PayRollManager',
            fields=[
                ('baseemployee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manager.baseemployee')),
            ],
            bases=('manager.baseemployee',),
        ),
        migrations.AddField(
            model_name='baseemployee',
            name='salary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.salary'),
        ),
    ]