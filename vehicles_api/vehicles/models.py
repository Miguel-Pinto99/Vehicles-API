from django.db import models
from django.utils.translation import gettext_lazy as _
from vehicles_api.owners.models import Owner

class Vehicle(models.Model):

    class CarType(models.TextChoices):
        CAR = 'CAR', _('Car')
        MOTOR = 'MOTOR', _('Motor')
        TRUCK = 'TRUCK', _('Truck')
        __empty__ = _("Other")

    type = models.CharField(
        max_length=5,
        choices=CarType.choices,
        default=CarType.CAR,
        help_text=_("The type of the vehicle"),
    )
    name = models.CharField(
        max_length=100,
        help_text=_("The name of the vehicle"),
    )
    year = models.IntegerField(
        help_text=_("The manufacturing year of the vehicle"),
    )
    type = models.CharField(
        _("vehicle type"),
        max_length=50,
        choices=CarType,
        help_text=_("The vehicle type"),
    )
    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        related_name='vehicles',
        help_text=_("The owner of the vehicle"),
    )