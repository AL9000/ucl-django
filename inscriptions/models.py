from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.datetime_safe import date


class User(AbstractUser):
    pass


class AcademicTraining(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


def date_must_be_future(value):
    if value and value <= date.today():
        raise ValidationError('The date must be future')


class InscriptionRequest(models.Model):
    candidat = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date_creation = models.DateField(auto_now_add=True)
    date_demande = models.DateField(validators=[date_must_be_future], null=True)
    date_modification = models.DateField(auto_now=True)
    accepted = models.BooleanField(default=False)
    trainings = models.ManyToManyField(AcademicTraining, related_name="requests")

    def __str__(self):
        return f"Demande numéro {self.id}"
