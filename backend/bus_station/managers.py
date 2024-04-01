from django.db import models
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseBadRequest
from .exceptions import SeatReservationError

def is_status_leaving_or_left(status):
    return status in ['leaving', 'left']
class BusManager(models.Manager):
    def get_all_buses(self):
        return self.all()

    def reserve_seat(self, bus_license_plate):
        bus = get_object_or_404(self.model, registration_plate=bus_license_plate)

        if is_status_leaving_or_left(bus.status):
            raise SeatReservationError("Bus is not accepting more reservations")

        if bus.seats_available > 0:
            bus.seats_available -= 1
            bus.save()
            return bus
        else:
            raise SeatReservationError("No available seats")

    def unreserve_seat(self, bus_license_plate):
        bus = get_object_or_404(self.model, registration_plate=bus_license_plate)

        if is_status_leaving_or_left(bus.status):
            raise SeatReservationError("Bus is not accepting reservation changes")

        if bus.seats_available < bus.max_seats:
            bus.seats_available += 1
            bus.save()
            return bus
        else:
            raise SeatReservationError("Bus is empty")
