# Generated by Django 5.0.12 on 2025-02-13 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0003_alter_vehicle_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the specification', max_length=100)),
                ('value', models.CharField(help_text='Enter the value of the specification', max_length=100)),
                ('vehicle', models.ForeignKey(help_text='Select the vehicle this specification belongs to', on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
