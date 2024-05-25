from enum import Enum
from django.db import models


# Create your models here.

class wypozyczalniaType(Enum):
    SPORT = "sport"
    VAN = "van"
    SUV = "suv"


    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]


class Auto(models.Model):
    AUTO_COLORS_CHOICES = [("RED", "red"), ("GREEN", "green"), ("BLACK", "black"), ("BLUE", "blue"), ("PINK", "pink"), ("ORANGE", "orange")]
    #UTO_BRAND_CHOICES = [("BMW", "bmw"),("AUDI", "audi"), ("MAZDA", 'mazda'),("VOLVO", "volvo"), ("SKODA", "skoda")]

    seats = models.PositiveSmallIntegerField()
    color = models.CharField(choices=AUTO_COLORS_CHOICES, max_length=16)
    #brand = models.CharField(max_length=20, choices=AUTO_BRAND_CHOICES, verbose_name="Car Brand")
    cargo = models.BooleanField(default=True)
    cup_holder = models.BooleanField(default=False)
    auto_type = models.CharField(choices=wypozyczalniaType.choices(), max_length=16)
    price_per_hour = models.DecimalField(decimal_places=2, max_digits=5)  # od 000.00 do 999.99

    def __str__(self):
        return f"{self.id}/{self.seats}/{self.auto_type}/{self.price_per_hour}"


class Klient(models.Model):
    mail = models.EmailField(unique=True)
    phone = models.CharField(max_length=16)
    birth_day = models.DateField()

    def __str__(self):
        return f"{self.id}/{self.mail}"

class Wynajem(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.PROTECT, related_name="rezerwuj")
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.klient.mail}/{self.auto}"

    def save(self, *args, **kwargs):
        hours = 1
        #TODO calculate hours from start to end
        self.price = self.auto.price_per_hour*hours
        super(Wynajem, self).save(*args, **kwargs)