from django.db import models
from apps.machines.models import Machine
from apps.sensors.models import Sensor

# Create your models here.

class Alert(models.Model):

    class Severity(models.TextChoices):
        LOW="LOW","Low"
        MEDIUM="MEDIUM","Medium"
        HIGH="HIGH", "High"

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="alerts"
    )

    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="alerts"
    )

    value = models.FloatField()

    threshold = models.FloatField()

    severity = models.CharField(
        max_length=10,
        choices=Severity
    )

    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.machine.name} - {self.severity}"
    