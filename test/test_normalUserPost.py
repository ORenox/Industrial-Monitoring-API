import pytest

@pytest.mark.django_db
def test_normal_user_cannot_create_machine(
    api_client,
    user,
):

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