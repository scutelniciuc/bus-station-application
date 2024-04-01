import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, RegexValidator
from .constants import BUS_STATUS_CHOICES

class User(AbstractUser):
    pass

class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birth_date = models.DateField(blank=True, null=True)
    years_of_experience = models.IntegerField(validators=[MinValueValidator(0)])
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Bus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    registration_plate = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z0-9]{2}-[A-Z0-9]{2}-[A-Z0-9]{2}$',
                message='Format must be XX-XX-XX',
                code='invalid_registration_plate'
            )
        ]
    )
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    end_destination = models.CharField(max_length=128)
    time_of_departure = models.DateTimeField()
    max_seats = models.IntegerField(validators=[MinValueValidator(8)])
    seats_available = models.IntegerField(validators=[MinValueValidator(0)])
    status = models.CharField(max_length=16, choices=BUS_STATUS_CHOICES)

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return f'Destination: {self.end_destination} - Departure: {self.time_of_departure.strftime("%H:%M %d-%m-%Y")}'