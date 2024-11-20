from django.urls import path
from exchange.views import CurrencyListView, ExchangeRateDetailView
from exchange.serializers import CurrencySerializer
from drf_yasg.utils import swagger_auto_schema

schema_view = swagger_auto_schema(
    view=CurrencyListView,
    operation_description="Retrieve a list of currencies",
    responses={200: CurrencySerializer(many=True)},
    tags=['Currency'],
)

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency-list'),
    path('currency/<str:base_code>/<str:target_code>/', ExchangeRateDetailView.as_view(), name='exchange-rate-detail'),
]
