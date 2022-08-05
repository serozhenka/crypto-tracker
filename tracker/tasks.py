import json
import requests

from celery import shared_task
from django.conf import settings

from .services import update_or_create_cryptos

@shared_task
def request_crypto_wrapper(every_n_seconds):
    for i in range(int(60 / every_n_seconds)):
        request_crypto.apply_async(countdown=i * every_n_seconds)

@shared_task
def request_crypto():
    url = f'https://api.nomics.com/v1/currencies/ticker?key={settings.NOMICS_API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    update_or_create_cryptos(data)