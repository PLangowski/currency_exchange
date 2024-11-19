from itertools import permutations
import yfinance as yf
from django.core.management.base import BaseCommand
from exchange.models import Currency, ExchangeRate


class Command(BaseCommand):
    help = "Load initial currency and exchange rate data"

    def handle(self, *args, **options):
        currencies = ['EUR', 'USD', 'JPY', 'PLN']
        currency_pairs = list(permutations(currencies, 2))

        for base, target in currency_pairs:
            pair = f"{base}{target}"
            try:
                data = yf.Ticker(f"{pair}=X").history(period="1d")
                if not data.empty:
                    rate = data['Close'].iloc[-1]
                    base_currency, _ = Currency.objects.get_or_create(code=base)
                    target_currency, _ = Currency.objects.get_or_create(code=target)
                    ExchangeRate.objects.update_or_create(
                        base_currency=base_currency,
                        target_currency=target_currency,
                        defaults={"exchange_rate": rate},
                        create_defaults={"exchange_rate": rate},
                    )
                    self.stdout.write(self.style.SUCCESS(f"Loaded {pair}: {rate}"))
                else:
                    self.stdout.write(self.style.WARNING(f"No data found for {pair}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error loading {pair}: {e}"))
