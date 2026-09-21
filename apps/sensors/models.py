from django.db import models

from apps.machines.models import Machine
# Create your models here.

class Sensor(models.Model):

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="sensors"
    )

    name = models.CharField(max_length=100)
    sensor_type = models.CharField(max_length=100)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name