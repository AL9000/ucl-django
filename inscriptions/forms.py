from django import forms
from django.contrib.auth import get_user_model

from inscriptions.models import InscriptionRequest, AcademicTraining


class InscriptionCreateForm(forms.ModelForm):
    date_demande = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = InscriptionRequest
        fields = ("candidat", "trainings", "date_demande")
