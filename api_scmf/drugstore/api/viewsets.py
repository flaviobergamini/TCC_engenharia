from rest_framework import viewsets
from drugstore.api import serializers
from drugstore import models

class DrugstoreViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DrugstoreSerializer
    queryset = models.Drugstore.objects.all()