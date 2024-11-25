from rest_framework import serializers
from simple_history.models import HistoricalRecords
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

class HistoricalExchangeRateSerializer(serializers.ModelSerializer):
    history_date = serializers.DateTimeField()
    base_currency = serializers.CharField(source='base_currency.code')
    target_currency = serializers.CharField(source='target_currency.code')
    class Meta:
        model = ExchangeRate.history.model
        fields = [
            "base_currency",
            "target_currency",
            "exchange_rate",
            "history_date",
        ]
