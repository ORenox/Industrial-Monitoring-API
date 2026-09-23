import pytest


@pytest.mark.django_db
def test_staff_user_can_create_machine(
    api_client,
    staff_user,
):

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