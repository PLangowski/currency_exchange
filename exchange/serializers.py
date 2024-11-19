from rest_framework import serializers
from exchange.models import Currency, ExchangeRate

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['code']

class ExchangeRateSerializer(serializers.ModelSerializer):
    currency_pair = serializers.SerializerMethodField()

    class Meta:
        model = ExchangeRate
        fields = ['currency_pair', 'exchange_rate']

    def get_currency_pair(self, obj):
        return f"{obj.base_currency.code}{obj.target_currency.code}"
