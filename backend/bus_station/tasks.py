from celery import shared_task
from bus_station.models import Bus, User
from django.core.mail import send_mail


@shared_task()
def task_check_bus_service():
    buses = Bus.objects.get_buses_for_service_alert_email()

    if buses.exists():
        for bus in buses:
            admins_emails = User.objects.get_all_admins_emails()

            subject = f'Bus {bus.id} needs service'
            message = f'Bus with registration plate {bus.registration_plate} will need service'
            from_email = 'system@mail.com'
            send_mail(subject, message, from_email, admins_emails)