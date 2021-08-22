from django.contrib import admin
from .models import Currency, CurrencyRate

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class CurrencyRatesAdmin(admin.ModelAdmin):
    def currency(obj):
        return obj.currency.name
    list_display = ('id', currency, 'date', 'rate')

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyRate, CurrencyRatesAdmin)
