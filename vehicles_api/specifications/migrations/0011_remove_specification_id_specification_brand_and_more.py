# Generated by Django 5.0.12 on 2025-02-14 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0010_remove_specification_brand_and_more'),
        ('vehicles', '0008_alter_vehicle_owner_alter_vehicle_plate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='id',
        ),
        migrations.AddField(
            model_name='specification',
            name='brand',
            field=models.CharField(default='Unknown', help_text='Enter the brand of the vehicle', max_length=100),
        ),
        migrations.AddField(
            model_name='specification',
            name='color',
            field=models.CharField(blank=True, default='Unknown', help_text='Enter the color of the vehicle', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specification',
            name='first_registry',
            field=models.IntegerField(blank=True, default=2000, help_text='Enter the year of the vehicle', null=True),
        ),
        migrations.AddField(
            model_name='specification',
            name='fuel',
            field=models.CharField(blank=True, default='Unknown', help_text='Enter the fuel type of the vehicle', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specification',
            name='model',
            field=models.CharField(blank=True, default='Unknown', help_text='Enter the model of the vehicle', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='specification',
            name='vehicle',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='specifications', serialize=False, to='vehicles.vehicle'),
            preserve_default=False,
        ),
    ]
