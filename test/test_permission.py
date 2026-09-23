import pytest


@pytest.mark.django_db
def test_normal_user_cannot_create_machine(api_client, user):
    api_client.force_authenticate(user=user)

    response = api_client.post(
        "/api/machines/",
        {
            "name": "CNC-999",
            "model": "Test Model",
            "location": "Factory Test",
        },
        format="json",
    )

    assert response.status_code == 403

@pytest.mark.django_db
def test_staff_user_can_create_machine(api_client, staff_user):
    api_client.force_authenticate(user=staff_user)

    response = api_client.post(
        "/api/machines/",
        {
            "name": "CNC-999",
            "model": "Test Model",
            "location": "Factory Test",
        },
        format="json",
    )

    assert response.status_code == 201

@pytest.mark.django_db
def test_normal_user_can_read_machines(api_client, user):
    api_client.force_authenticate(user=user)

    response = api_client.get("/api/machines/")

    assert response.status_code == 200

@pytest.mark.django_db
def test_unauthenticated_user_can_read_machines(api_client):
    response = api_client.get("/api/machines/")

    assert response.status_code == 200

@pytest.mark.django_db
def test_unauthenticated_user_cannot_create_machine(api_client):
    response = api_client.post(
        "/api/machines/",
        {
            "name": "CNC-999",
            "model": "Test Model",
            "location": "Factory Test",
        },
        format="json",
    )

    assert response.status_code == 401