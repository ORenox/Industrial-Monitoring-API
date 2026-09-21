from rest_framework import serializers

from apps.sensors.models import Sensor

class sensorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Sensor
        fields=[
            "id",
            "machine",
            "name",
            "sensor_type",
            "unit",
        ]