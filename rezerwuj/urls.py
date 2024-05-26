"""
URL configuration for wypozyczalnia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rezerwuj.views import AutoListView, AutoDetailView, confirm_reservation

urlpatterns = [
    path("wypozyczalnia/", AutoListView.as_view(), name="wypozyczalnia-list"), # 127.0.0.1:8000/rezerwuj/wypozyczalnia
    path("wypozyczalnia/<int:pk>/", AutoDetailView.as_view(), name="wypozyczalnia-detail"),
    #path("wypozyczalnia/<int:pk>/", AutoDetailView.as_view(), name="wypozyczalnia-detail")  # 127.0.0.1:8000/wypozyczalnia/[id_auta]/
    path("wypozyczalnia/<int:auto_id>/confirm_reservation/", confirm_reservation, name="wypozyczalnia-confirm-reservation") # 127.0.0.1:8000/wypozyczalnia/[id_auto]/
]