from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AcademicTraining(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class InscriptionRequest(models.Model):
    candidat = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_creation = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)
    accepted = models.BooleanField(default=False)
    trainings = models.ManyToManyField(AcademicTraining, related_name="requests")

    def __str__(self):
        return f"Demande numéro {self.id}"
