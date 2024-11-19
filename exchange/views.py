from rest_framework.views import APIView
from rest_framework.response import Response
from exchange.models import Currency, ExchangeRate
from exchange.serializers import CurrencySerializer, ExchangeRateSerializer
from django.shortcuts import get_object_or_404

class CurrencyListView(APIView):
    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

class ExchangeRateDetailView(APIView):
    def get(self, request, base_code, target_code):
        base_currency = get_object_or_404(Currency, code=base_code)
        target_currency = get_object_or_404(Currency, code=target_code)
        rate = ExchangeRate.objects.filter(base_currency=base_currency, target_currency=target_currency).first()
        if rate:
            serializer = ExchangeRateSerializer(rate)
            return Response(serializer.data)
        return Response({"error": "Exchange rate not found"}, status=404)
