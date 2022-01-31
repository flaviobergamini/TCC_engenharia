from django.db import models


class Doctor(models.Model):
    regional_council = models.CharField(primary_key=True, editable=True, max_length=20)
    specialty = models.CharField(max_length=30, editable=True, blank=True, null=True)
    name = models.CharField(max_length=45)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=45)
    street = models.CharField(max_length=45)
    complement = models.CharField(max_length=200,blank=True)
    number = models.IntegerField()
    cep = models.CharField(max_length=10, blank=True)
    cpf = models.CharField(max_length=14, blank=True)

