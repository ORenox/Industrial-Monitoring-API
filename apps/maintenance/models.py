from django.db import models

from django.contrib.auth.models import User
from apps.machines.models import Machine 
# Create your models here.

class Maintenance(models.Model):

    class MaintenanceType(models.TextChoices):
        PREVENTIVE = "PREVENTIVE", "Preventive"
        CORRECTIVE = "CORRECTIVE", "Corrective"

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="maintenance_records",
    )

    technician = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    maintenance_type = models.CharField(
        max_length=20,
        choices=MaintenanceType.choices,
    )

    description = models.TextField()

    scheduled_date = models.DateField()

    completed = models.BooleanField(default=False)

    completed_date = models.DateField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.machine.name} - {self.maintenance_type}"
