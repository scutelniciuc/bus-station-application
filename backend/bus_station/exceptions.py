from rest_framework.exceptions import APIException


class SeatReservationError(APIException):
    status_code = 400
    default_code = 'not possible to reserve seat'
