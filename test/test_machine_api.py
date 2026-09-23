
import pytest

from rest_framework.test import APIClient

from apps.machines.models import Machine

@pytest.mark.django_db
def test_get_machines(api_client,machine):

    response = api_client.get("/api/machines/")

    assert response.status_code == 200

@pytest.mark.django_db
def test_authenticated_get_machines(
    api_client,
    user,
    machine,
):

    api_client.force_authenticate(user=user)

    response = api_client.get("/api/machines/")

    assert response.status_code == 200