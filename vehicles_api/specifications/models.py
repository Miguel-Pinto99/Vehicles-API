from django.db import models
from vehicles_api.vehicles.models import Vehicle

class Specification(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the name of the specification")
    value = models.CharField(max_length=100, help_text="Enter the value of the specification")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, help_text="Select the vehicle this specification belongs to")