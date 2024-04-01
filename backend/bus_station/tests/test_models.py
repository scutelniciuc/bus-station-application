from datetime import date

import pytest
from django.core.exceptions import ValidationError
from .fixtures import driver_sample, bus_sample, driver_data, bus_data
from bus_station.models import Driver, Bus

@pytest.mark.django_db
class TestDriverModel:
    def test_create_driver(self, driver_data):
        driver = Driver(**driver_data)
        driver.full_clean()
        driver.save()

        assert isinstance(driver, Driver)
        assert driver.first_name == driver_data['first_name']
        assert driver.last_name == driver_data['last_name']
        assert driver.birth_date == driver_data['birth_date']
        assert driver.years_of_experience == driver_data['years_of_experience']
        assert driver.date_joined == driver_data['date_joined']

    def test_invalid_years_of_experience(self, driver_sample):
        driver_sample.years_of_experience = -1

        with pytest.raises(ValidationError):
            driver_sample.full_clean()

@pytest.mark.django_db
class TestBusModel:
    def test_create_bus(self, bus_data):
        bus = Bus(**bus_data)
        bus.full_clean()
        bus.save()

        assert isinstance(bus, Bus)
        assert bus.registration_plate == bus_data['registration_plate']
        assert bus.end_destination == bus_data['end_destination']
        assert bus.time_of_departure == bus_data['time_of_departure']
        assert bus.max_seats == bus_data['max_seats']
        assert bus.seats_available == bus_data['seats_available']
        assert bus.status == bus_data['status']

    def test_invalid_license_plate(self, bus_sample):
        bus_sample.registration_plate = "---"

        with pytest.raises(ValidationError):
            bus_sample.full_clean()