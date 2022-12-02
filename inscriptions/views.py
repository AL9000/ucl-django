from django.forms import modelformset_factory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

from inscriptions.filters import InscriptionRequestFilter
from inscriptions.forms import InscriptionCreateForm
from inscriptions.models import InscriptionRequest, AcademicTraining


def home_view(request):
    return HttpResponse("Bienvenue")


class CreateTraining(FormView):
    template_name = "inscriptions/academic_training_form.html"
    success_url = reverse_lazy("inscriptions:list")

    def get_form(self, form_class=None):
        TrainingFormSet = modelformset_factory(
            AcademicTraining, fields=("label",), extra=3
        )
        return TrainingFormSet(self.request.POST or None)


def add_training(request):
    TrainingFormSet = modelformset_factory(
        AcademicTraining, fields=("label", ), extra=3
    )
    formset = TrainingFormSet(request.POST or None)

    if formset.is_valid():
        formset.save()
        return HttpResponseRedirect(reverse("inscriptions:list"))

    return render(
        request, "inscriptions/academic_training_form.html", {"formset": formset}
    )


class InscriptionRequestListView(ListView):
    model = InscriptionRequest

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(accepted=False)
        return queryset.select_related("candidat").prefetch_related("trainings")


class InscriptionRequestDetailView(DetailView):
    model = InscriptionRequest


class InscriptionRequestCreateView(CreateView):
    template_name = "inscriptions/inscriptionrequest_form.html"
    form_class = InscriptionCreateForm
    success_url = reverse_lazy("inscriptions:list")


class InscriptionRequestUpdateView(UpdateView):
    model = InscriptionRequest
    template_name = "inscriptions/inscriptionrequest_form.html"
    form_class = InscriptionCreateForm
    success_url = reverse_lazy("inscriptions:list")


class InscriptionRequestSearchView(FilterView, ListView):
    model = InscriptionRequest
    template_name = "inscriptions/inscriptionrequest_search.html"
    filterset_class = InscriptionRequestFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data(object_list=object_list, **kwargs)
        context_data["say_hello"] = _("Hello!")
        return context_data
