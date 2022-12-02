from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django_filters.views import FilterView

from inscriptions.filters import InscriptionRequestFilter
from inscriptions.forms import InscriptionCreateForm
from inscriptions.models import InscriptionRequest


def home_view(request):
    return HttpResponse("Bienvenue")


class InscriptionRequestListView(ListView):
    model = InscriptionRequest

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(accepted=False)


class InscriptionRequestDetailView(DetailView):
    model = InscriptionRequest


class InscriptionRequestCreateView(CreateView):
    template_name = "inscriptions/inscriptionrequest_form.html"
    form_class = InscriptionCreateForm
    success_url = reverse_lazy("inscriptions:list")


class InscriptionRequestUpdateView(UpdateView):
    template_name = "inscriptions/inscriptionrequest_form.html"
    form_class = InscriptionCreateForm
    success_url = reverse_lazy("inscriptions:list")


class InscriptionRequestSearchView(FilterView, ListView):
    model = InscriptionRequest
    template_name = "inscriptions/inscriptionrequest_search.html"
    filterset_class = InscriptionRequestFilter
