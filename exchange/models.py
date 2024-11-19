from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code

class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, related_name="rates_base", on_delete=models.CASCADE)
    target_currency = models.ForeignKey(Currency, related_name="rates_target", on_delete=models.CASCADE)
    exchange_rate = models.FloatField()
    class Meta:
        unique_together = ('base_currency', 'target_currency')
        

    def __str__(self):
        return f"{self.base_currency}/{self.target_currency}: {self.exchange_rate}"
