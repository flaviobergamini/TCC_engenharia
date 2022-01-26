from django.db import models
from uuid import uuid4

from drugstore.models import Drugstore

class DrugstoreOrder(models.Model):
    idOrder = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    link_prescription = models.CharField(max_length=45)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=45, blank=True)
    street = models.CharField(max_length=45, blank=True)
    complement = models.CharField(max_length=200, blank=True)
    number = models.IntegerField(blank=True)
    cep = models.CharField(max_length=10, blank=True)
    drugstore_cnpj = models.ForeignKey(Drugstore, on_delete=models.CASCADE)
