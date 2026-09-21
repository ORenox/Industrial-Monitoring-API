from django.shortcuts import render
from rest_framework import viewsets
from apps.maintenance.models import Maintenance
from apps.maintenance.serializers import MaintenanceSerializer

from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MaintenanceViewSet(viewsets.ModelViewSet):

    queryset= Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [IsAuthenticated]

    