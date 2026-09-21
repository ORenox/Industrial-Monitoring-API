from django.shortcuts import render
from apps.measurements.models import Measurement
from apps.measurements.serializers import MeasurementSerializer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


# Create your views here.

class MeasurementViewSet(viewsets.ModelViewSet):

    
    serializer_class = MeasurementSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        queryset = Measurement.objects.select_related("sensor")

        sensor_id = self.request.query_params.get("sensor")
        min_value = self.request.query_params.get("min_value")
        max_value = self.request.query_params.get("max_value")

        if sensor_id:
            queryset = queryset.filter(sensor_id=sensor_id)

        #mediciones cuyo valor sea mayor o igual a 50.

        if min_value: 
            queryset = queryset.filter(value__gte=min_value)

        #mediciones cuyo valor sea menor o igual a 100.
        if max_value: 
                    queryset = queryset.filter(value__lte=max_value)



        return queryset

    

    