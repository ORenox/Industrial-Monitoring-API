import pytest

from apps.machines.models import Machine
from apps.sensors.models import Sensor

@pytest.mark.django_db
def test_sensor_belongs_to_machine(sensor, machine):

    assert sensor.machine == machine
    assert machine.sensors.count() == 1