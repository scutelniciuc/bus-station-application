# backend/bus_station/tests/test_models.py

import pytest
from datetime import date
from faker import Faker
from django.core.exceptions import ValidationError
from bus_station.models import Driver

fake = Faker()

@pytest.mark.django_db
class TestDriverModel:
    driver_data = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'birth_date': fake.date_of_birth(minimum_age=20, maximum_age=50),
        'years_of_experience': fake.random_int(min=0, max=20),
        'date_joined': date.today()
    }

    def test_driver_creation(self):
        driver = Driver(**self.driver_data)
        driver.full_clean()
        driver.save()

        assert driver.first_name == self.driver_data['first_name']
        assert driver.last_name == self.driver_data['last_name']
        assert driver.birth_date == self.driver_data['birth_date']
        assert driver.years_of_experience == self.driver_data['years_of_experience']
        assert driver.date_joined == self.driver_data['date_joined']

    def test_invalid_years_of_experience(self):
        self.driver_data['years_of_experience'] = -1

        with pytest.raises(ValidationError):
            Driver(**self.driver_data).full_clean()