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
    plate = models.CharField(
        max_length=10,
        unique=True,
        default='',
        help_text=_("The plate of the vehicle"),
    )
    owner = models.OneToOneField(
        Owner,
        on_delete=models.CASCADE,
        related_name='vehicles',
        help_text=_("The owner of the vehicle"),
        primary_key=True,

    )
