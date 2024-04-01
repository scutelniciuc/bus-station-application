# Generated by Django 5.0.3 on 2024-04-01 10:34

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bus_station', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birth_date', models.DateField(blank=True)),
                ('years_of_experience', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('date_joined', models.DateField()),
            ],
        ),
    ]
