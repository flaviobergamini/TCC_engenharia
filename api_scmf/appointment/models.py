from django.db import models
from uuid import uuid4

from client.models import Client
from doctor.models import Doctor

class Appointment(models.Model):
    idQuery = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    time = models.CharField(max_length=45)
    date = models.CharField(max_length=10, blank=True)
    in_person = models.BooleanField()
    call = models.CharField(max_length=45, blank=True, null=True)
    client_cpf = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    doctor_rc = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)