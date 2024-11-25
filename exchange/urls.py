from django.urls import path
from exchange.views import CurrencyListView, ExchangeRateDetailView, HistoricalExchangeRateView

urlpatterns = [
    path('currency/', CurrencyListView.as_view(), name='currency-list'),
    path('currency/<str:base_code>/<str:target_code>/', ExchangeRateDetailView.as_view(), name='exchange-rate-detail'),
    path('currency/historical', HistoricalExchangeRateView.as_view(), name="historical-exchange-rate")
]
