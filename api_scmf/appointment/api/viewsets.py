from rest_framework import viewsets
from appointment.api import serializers
from appointment import models

class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AppointmentSerializer
    queryset = models.Appointment.objects.all()