from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from exchange.models import Currency, ExchangeRate

@admin.register(Currency)
class CurrencyAdmin(SimpleHistoryAdmin):
    list_display = ['code']

@admin.register(ExchangeRate)
class ExchangeRateAdmin(SimpleHistoryAdmin):
    list_display = ['base_currency', 'target_currency', 'exchange_rate']
