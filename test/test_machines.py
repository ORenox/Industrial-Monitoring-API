import pytest
from apps.machines.models import Machine


@pytest.mark.django_db
def test_machine_name(machine):
    assert machine.name == "CNC-001"

@pytest.mark.django_db
def test_machine_status(machine):

    assert machine.status == Machine.Status.ACTIVE

#-----------------

@pytest.mark.django_db
def test_create_machine(machine):

    assert machine.name == "CNC-001"
    assert machine.model == "Haas VF-2"
    assert machine.location == "Factory A"

@pytest.mark.django_db
def test_machine_default_status(machine):


    assert machine.status == Machine.Status.ACTIVE