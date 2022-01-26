from rest_framework import viewsets
from doctor.api import serializers
from doctor import models

class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DoctorSerializer
    queryset = models.Doctor.objects.all()