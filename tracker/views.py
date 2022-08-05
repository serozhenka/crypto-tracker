import json
import requests

from django.shortcuts import render
from django.conf import settings

from .models import CryptoCurrency

def home_page(request):
    cryptos = CryptoCurrency.objects.all()[:100]
    return render(request, 'tracker/home.html', context={'cryptos': cryptos})
