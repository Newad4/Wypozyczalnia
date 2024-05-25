from django.contrib import admin

from rezerwuj.models import Auto, Klient, Wynajem

# Register your models here.

class AutoAdmin(admin.ModelAdmin):
    fields = ["id", "seats", "color", "cargo", "cup_holder", "auto_type", "price_per_hour"]
    list_display = ["id", "seats", "color", "cargo", "cup_holder", "auto_type", "price_per_hour"]
    readonly_fields = ["id"]

#"brand" do dodania jezeli wymyślimy jak to dodać do klasy

class KlientAdmin(admin.ModelAdmin):
    fields =  ["mail", "phone", "birth_day",]
    list_display = ["mail", "phone", "birth_day",]


class WynajemAdmin(admin.ModelAdmin):
    field = ["id", "date_created", "klient", "auto", "price"]
    list_display = ["id", "date_created", "klient", "auto", "price"]
    readonly_fields = ["id", "price", "date_created"]



admin.site.register(Auto, AutoAdmin)
admin.site.register(Klient, KlientAdmin)
admin.site.register(Wynajem, WynajemAdmin)