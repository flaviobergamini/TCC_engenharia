from rest_framework import viewsets
from drugstore_orders.api import serializers
from drugstore_orders import models

class DrugstoreOrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DrugstoreOrderSerializer
    queryset = models.DrugstoreOrder.objects.all()