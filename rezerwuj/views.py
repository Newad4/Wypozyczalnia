from django.shortcuts import render
from django.views.generic import ListView, DetailView

from rezerwuj.forms import ConfirmReservationForm
from rezerwuj.models import Auto
#from rezerwuj.forms import ConfirmReservationForm
#from rezerwuj.models import Auto

# Create your views here.


class AutoListView(ListView):
    model = Auto
    template_name = "wypozyczalnia_list.html"


class AutoDetailView(DetailView):
    model = Auto
    template_name = "wypozyczalnia_detail.html"


def confirm_reservation(request, auto_id):
    # REQUEST METHODS
    # GET
    # POST
    # PUT
    # DELETE

    if request.method == "POST":
        form = ConfirmReservationForm(request.POST)
        if form.is_valid():
            # our logic create reservation
            # redirect
            print("data ok")
        else:
            ValidationError("Form data invalid")
    else:
        form = ConfirmReservationForm()

    return render(request, "confirm_reservation.html", {"form": form})
