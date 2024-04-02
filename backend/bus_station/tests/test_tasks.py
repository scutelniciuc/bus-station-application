import celery
import pytest

from ..tasks import task_check_bus_service
from .fixtures import bus_sample, bus_data, driver_sample, driver_data, admin_sample
from django.utils import timezone
from django.core import mail

@pytest.mark.django_db
def test_task_check_bus_service_triggered(bus_sample, admin_sample):
    one_year_from_now = timezone.now() + timezone.timedelta(days=365)
    bus_sample.last_service = one_year_from_now
    bus_sample.save()

    task_check_bus_service()

    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == f'Bus {bus_sample.id} needs service'

@pytest.mark.django_db
def test_task_check_bus_service_not_triggered(admin_sample):

    task_check_bus_service()

    assert len(mail.outbox) == 0
