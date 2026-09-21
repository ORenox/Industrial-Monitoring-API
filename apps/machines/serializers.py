from rest_framework import serializers
from apps.machines.models import Machine


class MachineSerializer(serializers.ModelSerializer):

    class Meta:
        model=Machine
        fields= [
            "id",
            "name",
            "model",
            "location",
            "status",
        ]