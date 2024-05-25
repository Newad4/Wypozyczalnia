from django.shortcuts import render
from django.views.generic import ListView

from rezerwuj.models import Auto

# Create your views here.


class AutoListView(ListView):
    model = Auto
    template_name = "wypozyczalnia_list.html"
