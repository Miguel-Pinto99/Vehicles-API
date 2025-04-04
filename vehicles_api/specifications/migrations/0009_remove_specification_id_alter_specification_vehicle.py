# Generated by Django 5.0.12 on 2025-02-14 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0008_remove_specification_plate_specification_vehicle'),
        ('vehicles', '0004_alter_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='id',
        ),
        migrations.AlterField(
            model_name='specification',
            name='vehicle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='specifications', serialize=False, to='vehicles.vehicle', to_field='plate'),
        ),
    ]
