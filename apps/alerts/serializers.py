from rest_framework import serializers
from apps.alerts.models import Alert

class AlertSerializer(serializers.Serializer):

    class Meta:
        model = Alert
        fields = [
            "id",
            "value",
            "threshold",
            "severity",
            "resolved",
            "created_at",
        ]
