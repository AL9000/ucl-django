from django import forms
from django.contrib.auth import get_user_model

from inscriptions.models import InscriptionRequest, AcademicTraining


class InscriptionCreateForm(forms.ModelForm):
    class Meta:
        model = InscriptionRequest
        fields = ("candidat", "trainings")


class InscriptionRequestSearchForm(forms.Form):
    text_search = forms.CharField(max_length=100, required=False)
    candidat = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False)
    trainings = forms.ModelMultipleChoiceField(queryset=AcademicTraining.objects.all(), required=False)
    accepted = forms.NullBooleanField(required=False)
