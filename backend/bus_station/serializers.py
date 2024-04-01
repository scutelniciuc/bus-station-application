from rest_framework import serializers
from .models import Bus


class BusSerializer(serializers.ModelSerializer):
    driver = serializers.SerializerMethodField()

    class Meta:
        model = Bus
        fields = '__all__'

    def get_driver(self, obj):
        driver = obj.driver
        return f"{driver.first_name} {driver.last_name}"
