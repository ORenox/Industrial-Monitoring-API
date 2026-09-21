from django.shortcuts import render
from rest_framework import viewsets
from apps.machines.models import Machine
from apps.machines.serializers import MachineSerializer

from apps.permissions import IsAdminOrReadOnly


#JWT
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class MachineViewSet(viewsets.ModelViewSet):

    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

    permission_classes = [IsAdminOrReadOnly]
