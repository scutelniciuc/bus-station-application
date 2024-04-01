from django.urls import path
from .views import BusList, ReserveSeat, UnreserveSeat

urlpatterns = [
    path('bus-list/', BusList.as_view(), name="bus-list"),
    path('bus/<str:bus_license_plate>/reserve-seat/', ReserveSeat.as_view(), name="reserve-seat"),
    path('bus/<str:bus_license_plate>/unreserve-seat/', UnreserveSeat.as_view(), name="unreserve-seat"),
]