from rest_framework import viewsets
from client.api import serializers
from client import models

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()