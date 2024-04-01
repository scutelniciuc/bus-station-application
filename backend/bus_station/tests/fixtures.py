import pytest
from faker import Faker
from bus_station.models import Driver, Bus
from datetime import date

fake = Faker()

@pytest.fixture
def driver_data():
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'birth_date': fake.date_of_birth(minimum_age=20, maximum_age=50),
        'years_of_experience': fake.random_int(min=0, max=20),
        'date_joined': date.today()
    }

@pytest.fixture
def driver_sample(driver_data):
    return Driver.objects.create(**driver_data)

@pytest.fixture
def bus_data(driver_sample):
    max_seats = fake.random_int(min=8, max=60)
    return {
        'registration_plate': fake.license_plate(),
        'driver': driver_sample,
        'end_destination': fake.address(),
        'time_of_departure': fake.date_time_between(start_date='now', end_date='+30d'),
        'max_seats': max_seats,
        'seats_available': max_seats,
        'status': fake.random_element(elements=['on_platform', 'arriving', 'leaving', 'left'])
    }

@pytest.fixture
def bus_sample(bus_data):
    return Bus.objects.create(**bus_data)