from django.contrib import admin

from .models import CryptoCurrency


class CryptoCurrencyAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'name', 'rank', 'price', 'market_cap')


admin.site.register(CryptoCurrency, CryptoCurrencyAdmin)