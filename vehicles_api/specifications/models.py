from django.db import models
from ..vehicles.models import Vehicle

class Specification(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE, to_field='plate', related_name='specifications', primary_key=True)
    brand = models.CharField(max_length=100, help_text="Enter the brand of the vehicle", default="Unknown")
    model = models.CharField(max_length=100, help_text="Enter the model of the vehicle", default="Unknown", null=True, blank=True)
    first_registry = models.IntegerField(help_text="Enter the year of the vehicle", default=2000, null=True, blank=True)
    fuel = models.CharField(max_length=100, help_text="Enter the fuel type of the vehicle", default="Unknown", null=True, blank=True)
    color = models.CharField(max_length=100, help_text="Enter the color of the vehicle", default="Unknown", null=True, blank=True)
