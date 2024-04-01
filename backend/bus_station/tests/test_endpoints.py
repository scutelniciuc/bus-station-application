import pytest
from django.urls import reverse
from .fixtures import client, bus_data, driver_data, driver_sample, bus_sample_for_reservations

@pytest.mark.django_db
def test_bus_list_view(client):
    url = reverse('bus-list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_reserve_seat_view(client, bus_sample_for_reservations):
    url = reverse('reserve-seat', kwargs={'bus_license_plate': bus_sample_for_reservations.registration_plate})
    response = client.post(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_unreserve_seat_view(client, bus_sample_for_reservations):
    url = reverse('unreserve-seat', kwargs={'bus_license_plate': bus_sample_for_reservations.registration_plate})
    response = client.post(url)
    assert response.status_code == 200