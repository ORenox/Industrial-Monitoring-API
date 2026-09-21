from rest_framework import serializers

from apps.maintenance.models import Maintenance

class MaintenanceSerializer(serializers.Serializer):

    class Meta:
        model=Maintenance

        fields=[
            "id",
            "machine",
            "technician",
            "maintenance_type",
            "description",
            "scheduled_date",
            "completed",
            "completed_date",
        ]


        def validate(self, data):
            completed = data.get("completed")
            completed_date = data.get("completed_date")

            if completed and not completed_date:
                raise serializers.ValidationError(
                    "Completed maintenance must have a completed date."
                )
            if not completed and completed_date:
                raise serializers.ValidationError(
                    "Incomplete maintenance cannot have a completed date."
                )
            return data