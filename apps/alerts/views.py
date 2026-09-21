from django.shortcuts import render
from rest_framework import viewsets
from apps.alerts.serializers import AlertSerializer
from apps.alerts.models import Alert

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class AlertViewSet(viewsets.ModelViewSet):

    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

    permission_classes = [IsAuthenticated]