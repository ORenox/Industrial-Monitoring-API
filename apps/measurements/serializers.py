from apps.measurements.models import Measurement
from rest_framework import serializers

#nested serializer
from apps.sensors.serializers import sensorSerializer

from django.utils import timezone

class MeasurementSerializer(serializers.ModelSerializer):

    # nested serializer sensor
    sensor_detail= sensorSerializer(
        source="sensor",
        read_only=True,
        )

    class Meta:
        model=Measurement
        fields = [
        'id',
        'sensor',
        'sensor_detail',
        'value',
        'timestamp',
        ]

    def validate_value(self, value):
        if value<0:
            raise serializers.ValidationError(
                "Measurement value can not be negative"
            )

        if value > 1000:
            raise serializers.ValidationError(
                            "Measurement value can not exceed 1000"
                )
        return value

    def validate(self, data):
        if data["timestamp"] > timezone.now():
            raise serializers.ValidationError(
                "Measurement timestamp cannot be in the future."
            )
        return data

    