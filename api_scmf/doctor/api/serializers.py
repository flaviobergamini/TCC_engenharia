from rest_framework import serializers
from doctor import models

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = '__all__'