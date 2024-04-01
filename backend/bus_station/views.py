from rest_framework import generics
from .models import Bus
from .serializers import BusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class BusList(generics.ListAPIView):
    queryset = Bus.objects.get_all_buses()
    serializer_class = BusSerializer

class ReserveSeat(APIView):
    def post(self, request, bus_license_plate):
        bus = Bus.objects.reserve_seat(bus_license_plate)
        serializer = BusSerializer(bus)
        return Response(serializer.data)

class UnreserveSeat(APIView):
    def post(self, request, bus_license_plate):
        bus = Bus.objects.unreserve_seat(bus_license_plate)
        serializer = BusSerializer(bus)
        return Response(serializer.data)