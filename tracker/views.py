from django.shortcuts import render

from .models import CryptoCurrency

def home_page(request):
    cryptos = CryptoCurrency.objects.all()[:100]
    return render(request, 'tracker/home.html', context={'cryptos': cryptos})
