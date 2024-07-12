from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms

class ProteinListView(generic.ListView):
    model = models.protein
    form_class = forms.ProteinForm
    context_object_name = "proteins"


class ProteinCreateView(generic.CreateView):
    model = models.protein
    form_class = forms.ProteinForm


class ProteinDetailView(generic.DetailView):
    model = models.protein
    form_class = forms.ProteinForm


class ProteinUpdateView(generic.UpdateView):
    model = models.protein
    form_class = forms.ProteinForm
    #fields=["protein_name"]
    pk_url_kwarg = "pk"


class ProteinDeleteView(generic.DeleteView):
    model = models.protein
    success_url = reverse_lazy("proteinapp_protein_list")

