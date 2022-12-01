import django_filters
from django_filters.widgets import RangeWidget

from inscriptions.models import InscriptionRequest


class InscriptionRequestFilter(django_filters.FilterSet):
    date_creation = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))
    date_modification = django_filters.DateFromToRangeFilter(widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = InscriptionRequest
        fields = [
            "candidat",
            "date_creation",
            "date_modification",
            "accepted",
            "trainings",
        ]
