# Generated by Django 5.0.12 on 2025-02-14 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0007_rename_year_specification_first_registry'),
        ('vehicles', '0004_alter_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='plate',
        ),
        migrations.AddField(
            model_name='specification',
            name='vehicle',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='specifications', to='vehicles.vehicle', to_field='plate'),
            preserve_default=False,
        ),
    ]
