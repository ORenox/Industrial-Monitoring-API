import pytest


@pytest.mark.django_db
def test_obtain_jwt_token(api_client,user):
    response = api_client.post(
        "/api/token/",
        {
            "username": "testuser",
            "password": "testpassword123",
        },
        format="json",
    )

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_obtain_jwt_token_with_invalid_password(api_client, user):
    response = api_client.post(
        "/api/token/",
        {
            "username": "testuser",
            "password": "wrong_password",
        },
        format="json",
    )

    assert response.status_code == 401

@pytest.mark.django_db
def test_obtain_jwt_token_with_unknown_user(api_client):
    response = api_client.post(
        "/api/token/",
        {
            "username": "does_not_exist",
            "password": "testpassword123",
        },
        format="json",
    )

    assert response.status_code == 401