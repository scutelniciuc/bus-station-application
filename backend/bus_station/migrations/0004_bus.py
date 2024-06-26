# Generated by Django 5.0.3 on 2024-04-01 10:58

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_station', '0003_alter_driver_birth_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('registration_plate', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='invalid_registration_plate', message='Format must be NN-LL-NN', regex='^\\d{2}-[A-Z]{2}-\\d{2}$')])),
                ('end_destination', models.CharField(max_length=128)),
                ('time_of_departure', models.DateTimeField()),
                ('max_seats', models.IntegerField(validators=[django.core.validators.MinValueValidator(8)])),
                ('seats_available', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('status', models.CharField(choices=[('on_platform', 'On platform'), ('arriving', 'Arriving'), ('leaving', 'Leaving'), ('left', 'Left')], max_length=16)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus_station.driver')),
            ],
        ),
    ]
