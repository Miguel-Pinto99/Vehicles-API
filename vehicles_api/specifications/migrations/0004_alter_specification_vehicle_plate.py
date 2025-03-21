# Generated by Django 5.0.12 on 2025-02-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specifications', '0003_remove_specification_vehicle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='vehicle_plate',
            field=models.CharField(default='Unknown', help_text='Enter the plate of the vehicle', max_length=100),
        ),
    ]
