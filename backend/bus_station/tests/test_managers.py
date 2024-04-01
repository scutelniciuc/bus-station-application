import pytest
from .fixtures import driver_sample, bus_sample, bus_sample_2, bus_sample_full, driver_data, bus_data, bus_sample_for_reservations
from bus_station.models import Driver, Bus
from bus_station.exceptions import SeatReservationError

@pytest.mark.django_db
class TestBusManager:
    def test_get_all_buses(self, bus_sample, bus_sample_2):
        queryset = Bus.objects.get_all_buses()

        assert queryset.count() == 2
        assert bus_sample in queryset
        assert bus_sample_2 in queryset

    def test_reserve_seat(self, bus_sample_for_reservations):
        seats_available = bus_sample_for_reservations.seats_available

        Bus.objects.reserve_seat(bus_sample_for_reservations.registration_plate)
        bus_sample_for_reservations.refresh_from_db()

        assert bus_sample_for_reservations.seats_available == seats_available - 1

    def test_reserve_seat_raises_error_when_full(self, bus_sample_full):
        with pytest.raises(SeatReservationError):
            Bus.objects.reserve_seat(bus_sample_full.registration_plate)

    def test_reserve_seat_raises_error_on_left_status(self, bus_sample_for_reservations):
        bus_sample_for_reservations.status = "left"
        bus_sample_for_reservations.save()

        with pytest.raises(SeatReservationError):
            Bus.objects.reserve_seat(bus_sample_for_reservations.registration_plate)

    def test_unreserve_seat(self, bus_sample_for_reservations):
        seats_available = bus_sample_for_reservations.seats_available

        Bus.objects.unreserve_seat(bus_sample_for_reservations.registration_plate)
        bus_sample_for_reservations.refresh_from_db()

        assert bus_sample_for_reservations.seats_available == seats_available + 1

    def test_reserve_seat_raises_error_when_empty(self, bus_sample_for_reservations):
        bus_sample_for_reservations.seats_available = bus_sample_for_reservations.max_seats
        bus_sample_for_reservations.save()

        with pytest.raises(SeatReservationError):
            Bus.objects.unreserve_seat(bus_sample_for_reservations.registration_plate)