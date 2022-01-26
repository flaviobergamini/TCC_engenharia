from django.db import models

from client.models import Client

class Drugstore(models.Model):
    cnpj = models.CharField(primary_key=True, editable=True, max_length=20)
    name = models.CharField(max_length=45)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    complement = models.CharField(max_length=200, blank=True)
    number = models.IntegerField(blank=True)
    cep = models.CharField(max_length=10, blank=True)
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
