from rest_framework import serializers
from drugstore import models

class DrugstoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Drugstore
        fields = '__all__'