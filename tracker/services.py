from .models import CryptoCurrency


def update_or_create_cryptos(info_list):
    for info in info_list:
        exists, kwargs = True, {}
        try:
            CryptoCurrency.objects.get(identifier=info.get('id'))
        except CryptoCurrency.DoesNotExist:
            exists = False
            kwargs.update({
                'identifier': info.get('id'),
                'name': info.get('name'),
                'logo_url': info.get('logo_url'),
            })

        kwargs.update({
            'rank': info.get('rank'),
            'price': info.get('price'),
            'market_cap': info.get('market_cap'),
            'circulating_supply': info.get('circulating_supply'),
            'max_supply': info.get('max_supply'),
            'price_change_pct_1d': info.get('1d').get('price_change_pct'),
            'price_change_pct_7d': info.get('7d').get('price_change_pct'),
            'price_change_pct_30d': info.get('30d').get('price_change_pct'),
            'price_change_pct_365d': info.get('365d').get('price_change_pct'),
        })

        if not exists:
            CryptoCurrency.objects.create(**kwargs)
        else:
            CryptoCurrency.objects.filter(identifier=info.get('id')).update(**kwargs)
