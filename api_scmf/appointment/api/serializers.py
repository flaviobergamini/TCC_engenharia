from rest_framework import serializers
from appointment import models

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = '__all__'