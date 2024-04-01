from django.urls import path
from .views import BusList, ReserveSeat, UnreserveSeat

urlpatterns = [
    path('bus-list/', BusList.as_view()),
    path('bus/<str:bus_license_plate>/reserve-seat/', ReserveSeat.as_view()),
    path('bus/<str:bus_license_plate>/unreserve-seat/', UnreserveSeat.as_view()),
]