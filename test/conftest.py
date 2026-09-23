import pytest

from apps.machines.models import Machine
from apps.measurements.models import Measurement
from apps.sensors.models import Sensor
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def user():
    return User.objects.create_user(
        username="testuser",
        password="testpassword123",
    )

@pytest.fixture
def api_client():

    return APIClient()

@pytest.fixture
def staff_user():

    return User.objects.create_user(
        username="staffuser",
        password="staffpassword123",
        is_staff=True,
    )


@pytest.fixture
def machine():
    return Machine.objects.create(
        name="CNC-001",
        model="Haas VF-2",
        location="Factory A",
    )

@pytest.fixture
def sensor(machine):

    return Sensor.objects.create(
        machine=machine,
        name="Temperature Sensor",
        sensor_type="TEMPERATURE",
        unit="C",
    )

@pytest.fixture
def measurement(sensor):

    return Measurement.objects.create(
        sensor=sensor,
        value=75.5,
        timestamp="2026-09-20T15:00:00Z",
    )