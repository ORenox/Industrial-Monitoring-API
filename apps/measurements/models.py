from django.db import models

from apps.sensors.models import Sensor
# Create your models here.

class Measurement(models.Model):

    sensor=models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="measurements"
    )
    value = models.FloatField()
    timestamp = models.DateTimeField()


    def __str__(self):
        return f"{self.sensor.name}: {self.value}"
