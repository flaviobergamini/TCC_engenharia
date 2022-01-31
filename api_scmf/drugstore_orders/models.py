from distutils.command.upload import upload
from django.db import models
from uuid import uuid4

from client.models import Client
from drugstore.models import Drugstore

def upload_image_prescription(instance, filename):
    return f'{instance.idOrder}-{filename}'

class DrugstoreOrder(models.Model):
    idOrder = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    state = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=45, blank=True)
    street = models.CharField(max_length=45, blank=True)
    complement = models.CharField(max_length=200, blank=True)
    number = models.IntegerField(blank=True)
    cep = models.CharField(max_length=10, blank=True)
    image = models.ImageField(upload_to=upload_image_prescription, blank=True, null=True)
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    drugstore_cnpj = models.ForeignKey(Drugstore, on_delete=models.CASCADE, blank=True, null=True)
