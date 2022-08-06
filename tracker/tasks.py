import json
import requests

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from django.conf import settings

from .services import update_or_create_cryptos

channel_layer = get_channel_layer()


@shared_task
def request_crypto_wrapper(every_n_seconds):
    for i in range(int(60 / every_n_seconds)):
        request_crypto.apply_async(countdown=i * every_n_seconds)

@shared_task
def request_crypto():
    url = f'https://api.nomics.com/v1/currencies/ticker?key={settings.NOMICS_API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    async_to_sync(channel_layer.group_send)('crypto', {
        'type': 'tracker.send_data',
        'data': data,
    })

    update_or_create_cryptos(data)

