# Generated by Django 5.0.12 on 2025-02-14 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
        ('vehicles', '0005_alter_vehicle_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='id',
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='owner',
            field=models.OneToOneField(help_text='The owner of the vehicle', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='vehicle', serialize=False, to='owners.owner'),
        ),
    ]
