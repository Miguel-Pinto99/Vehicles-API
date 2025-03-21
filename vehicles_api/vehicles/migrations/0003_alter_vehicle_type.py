# Generated by Django 5.0.12 on 2025-02-13 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_remove_vehicle_name_remove_vehicle_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='type',
            field=models.CharField(choices=[(None, 'Other'), ('CAR', 'Car'), ('MOTOR', 'Motor'), ('TRUCK', 'Truck')], default='Other', help_text='The type of the vehicle', max_length=5),
        ),
    ]
