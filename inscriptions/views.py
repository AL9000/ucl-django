from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormMixin

from inscriptions.forms import InscriptionCreateForm, InscriptionRequestSearchForm
from inscriptions.models import InscriptionRequest


def home_view(request):
    return HttpResponse("Bienvenue")


class InscriptionRequestListView(ListView):
    model = InscriptionRequest


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


def search_inscriptions(request):
    search_form = InscriptionRequestSearchForm(request.GET or None)
    inscriptions = InscriptionRequest.objects.all()
    if search_form.is_valid():
        inscriptions = inscriptions.filter(candidat=search_form.cleaned_data.get('candidat'))
    return render(
        request,
        "inscriptions/inscriptionrequest_search.html",
        {"form": search_form, "inscriptions": inscriptions}
    )


class InscriptionRequestSearchView(ListView):
    model = InscriptionRequest
    template_name = "inscriptions/inscriptionrequest_search.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = InscriptionRequestSearchForm(self.request.GET or None)

        if search_form.is_valid():
            candidat = search_form.cleaned_data.get("candidat")
            trainings = search_form.cleaned_data.get("trainings")
            accepted = search_form.cleaned_data.get("accepted")
            text_search = search_form.cleaned_data.get("text_search")

            if candidat:
                queryset = queryset.filter(candidat=candidat)
            if trainings:
                queryset = queryset.filter(trainings__in=trainings)
            if accepted in [False, True]:
                queryset = queryset.filter(accepted=accepted)
            if text_search:
                queryset = queryset.filter(
                    Q(candidat__username__icontains=text_search) |
                    Q(trainings__label__icontains=text_search)
                )

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['form'] = InscriptionRequestSearchForm(self.request.GET or None)
        context.update({"form": InscriptionRequestSearchForm(self.request.GET or None)})
        return context
