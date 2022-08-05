import json
import requests

from django.shortcuts import render
from django.conf import settings

from .models import CryptoCurrency

def home_page(request):
    url = f'https://api.nomics.com/v1/currencies/ticker?key={settings.NOMICS_API_KEY}'

    response = requests.get(url)
    data = json.loads(response.text)
    # result = json.dumps(data)
    from .services import update_or_create_cryptos
    update_or_create_cryptos(data)

    cryptos = CryptoCurrency.objects.all()[:100]
    return render(request, 'tracker/home.html', context={'cryptos': cryptos})
