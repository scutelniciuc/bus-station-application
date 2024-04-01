import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

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