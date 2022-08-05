from django.db import models


class CryptoCurrency(models.Model):
    identifier = models.CharField(max_length=16)
    rank = models.SmallIntegerField()
    name = models.CharField(max_length=128)
    logo_url = models.URLField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    market_cap = models.BigIntegerField()
    circulating_supply = models.BigIntegerField()
    max_supply = models.BigIntegerField(null=True)

    price_change_pct_1d = models.DecimalField(max_digits=9, decimal_places=4)
    price_change_pct_7d = models.DecimalField(max_digits=9, decimal_places=4)
    price_change_pct_30d = models.DecimalField(max_digits=9, decimal_places=4)
    price_change_pct_365d = models.DecimalField(max_digits=9, decimal_places=4)

    class Meta:
        verbose_name_plural = 'Crypto currencies'
        ordering = ['rank']

    def __str__(self):
        return self.identifier

    @property
    def circulating_supply_ptc(self):
        if self.max_supply:
            return self.circulating_supply / self.max_supply * 100
        return 100
