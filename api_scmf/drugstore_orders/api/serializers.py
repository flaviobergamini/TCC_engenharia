from rest_framework import serializers
from drugstore_orders import models

class DrugstoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DrugstoreOrder
        fields = '__all__'