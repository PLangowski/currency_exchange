from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from exchange.models import Currency, ExchangeRate
from exchange.serializers import CurrencySerializer, ExchangeRateSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

class CurrencyListView(ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ['code']
    ordering = ['code']

    @swagger_auto_schema(
        operation_description="Retrieve a list of currencies",
        responses={200: CurrencySerializer(many=True)},
        tags=['Currency'],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ExchangeRateDetailView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve the exchange rate for given currencies",
        responses={200: ExchangeRateSerializer()},
        tags=['Currency'],
    )
    def get(self, request, base_code, target_code):
        base_currency = get_object_or_404(Currency, code=base_code)
        target_currency = get_object_or_404(Currency, code=target_code)
        rate = ExchangeRate.objects.filter(base_currency=base_currency, target_currency=target_currency).first()
        if rate:
            serializer = ExchangeRateSerializer(rate)
            return Response(serializer.data)
        return Response({"error": "Exchange rate not found"}, status=404)
