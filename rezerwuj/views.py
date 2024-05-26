from django.shortcuts import render
from django.views.generic import ListView, DetailView

from rezerwuj.models import Auto

# Create your views here.


class AutoListView(ListView):
    model = Auto
    template_name = "wypozyczalnia_list.html"


class AutoDetailView(DetailView):
    model = Auto
    template_name = "wypozyczalnia_detail.html"