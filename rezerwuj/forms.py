from django import forms


class ConfirmReservationForm(forms.Form):
    mail = forms.EmailField()
    phone = forms.CharField(max_length=16)
    age = forms.IntegerField()