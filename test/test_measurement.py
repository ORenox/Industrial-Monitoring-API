import pytest
from django.utils import timezone
from apps.measurements.models import Measurement

@pytest.mark.django_db
def test_create_measurement(api_client, sensor, staff_user):

    api_client.force_authenticate(user=staff_user)

    response = api_client.post(
        "/api/measurements/",
        {
            "sensor": sensor.id,
            "value": 75.5,
            "timestamp": "2026-09-20T15:00:00Z",
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["sensor"] == sensor.id
    assert float(response.data["value"]) == 75.5

@pytest.mark.django_db
def test_measurement_value_cannot_be_negative(api_client, sensor, staff_user):

    api_client.force_authenticate(user=staff_user)
    response = api_client.post(
        "/api/measurements/",
        {
            "sensor": sensor.id,
            "value": -10,
            "timestamp": "2026-09-20T15:00:00Z",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "value" in response.data

@pytest.mark.django_db
def test_measurement_value_cannot_exceed_1000(api_client, sensor, staff_user):

    api_client.force_authenticate(user=staff_user)
    response = api_client.post(
        "/api/measurements/",
        {
            "sensor": sensor.id,
            "value": 1001,
            "timestamp": "2026-09-20T15:00:00Z",
        },
        format="json",
    )

    assert response.status_code == 400
    assert "value" in response.data

@pytest.mark.django_db
def test_measurement_timestamp_cannot_be_in_future(api_client, sensor, staff_user):

    api_client.force_authenticate(user=staff_user)
    future_timestamp = timezone.now() + timezone.timedelta(hours=1)

    response = api_client.post(
        "/api/measurements/",
        {
            "sensor": sensor.id,
            "value": 75.5,
            "timestamp": future_timestamp.isoformat(),
        },
        format="json",
    )

    assert response.status_code == 400
    assert "non_field_errors" in response.data

@pytest.mark.django_db
def test_filter_measurements_by_sensor(
    api_client,
    sensor,
    measurement,
    user
):
    api_client.force_authenticate(user=user)
    response = api_client.get(
        f"/api/measurements/?sensor={sensor.id}"
    )

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["sensor"] == sensor.id

@pytest.mark.django_db
def test_filter_measurements_by_min_value(
    api_client,
    sensor,
    measurement,
    staff_user
):
    api_client.force_authenticate(user=staff_user)
    Measurement.objects.create(
        sensor=sensor,
        value=30,
        timestamp="2026-09-20T16:00:00Z",
    )

    response = api_client.get(
        "/api/measurements/?min_value=50"
    )

    assert response.status_code == 200
    assert len(response.data) == 1
    assert float(response.data[0]["value"]) >= 50


@pytest.mark.django_db
def test_filter_measurements_by_max_value(
    api_client,
    sensor,
    measurement,
    user
):
    api_client.force_authenticate(user=user)
    Measurement.objects.create(
        sensor=sensor,
        value=30,
        timestamp="2026-09-20T16:00:00Z",
    )

    response = api_client.get(
        "/api/measurements/?max_value=50"
    )

    assert response.status_code == 200
    assert len(response.data) == 1
    assert float(response.data[0]["value"]) <= 50