from django.db import models
from uuid import uuid4

from doctor.models import Doctor

class Appointment(models.Model):
    idQuery = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    time = models.CharField(max_length=45)
    in_person = models.BooleanField()
    call = models.CharField(max_length=45, blank=True)
    doctor_crm = models.ForeignKey(Doctor, on_delete=models.CASCADE)
