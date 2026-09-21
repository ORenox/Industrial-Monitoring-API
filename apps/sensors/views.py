from django.shortcuts import render

from rest_framework import viewsets
from apps.sensors.models import Sensor
from apps.sensors.serializers import sensorSerializer

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = sensorSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):

        queryset = Sensor.objects.all()

        machine_id = self.request.query_params.get("machine")
        sensor_type = self.request.query_params.get("type")

        search = self.request.query_params.get("search")

        if machine_id:
            queryset = queryset.filter(machine_id = machine_id)

        if sensor_type:
            queryset = queryset.filter(sensor_type=sensor_type)

        if search: 
            queryset = queryset.filter(name__icontains=search)


        
        return queryset