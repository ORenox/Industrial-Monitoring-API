from django.db import models

# Create your models here.

class Machine(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        MAINTENANCE = "MAINTENANCE", "Maintenance"
        OFFLINE = "OFFLINE", "Offline"

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    def __str__(self):
        return self.name
