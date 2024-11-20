from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from exchange.models import Currency, ExchangeRate
from exchange.serializers import ExchangeRateSerializer

class CurrencyListViewTests(APITestCase):
    def setUp(self):
        Currency.objects.create(code='USD')
        Currency.objects.create(code='EUR')
        Currency.objects.create(code='JPY')

    def test_list_currencies(self):
        """
        GET /currency returns a list of all currencies in the database.
        """
        url = reverse('currency-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertIn({'code': 'USD'}, response.data)
        self.assertIn({'code': 'EUR'}, response.data)
        self.assertIn({'code': 'JPY'}, response.data)

    def test_list_currencies_default_ordering(self):
        """
        Currencies are sorted by code (default)
        """
        url = reverse('currency-list')
        response = self.client.get(url)

        codes = [currency['code'] for currency in response.data]
        self.assertEqual(codes, sorted(codes))

    def test_list_currencies_reverse_ordering(self):
        """
        Currencies can be sorted in reverse order
        """
        url = reverse('currency-list') + '?ordering=-code'
        response = self.client.get(url)

        codes = [currency['code'] for currency in response.data]
        self.assertEqual(codes, sorted(codes, reverse=True))

class ExchangeRateDetailViewTest(APITestCase):
    def setUp(self):
        self.usd = Currency.objects.create(code="USD")
        self.eur = Currency.objects.create(code="EUR")
        self.jpy = Currency.objects.create(code="JPY")
        
        self.exchange_rate = ExchangeRate.objects.create(
            base_currency=self.usd,
            target_currency=self.eur,
            exchange_rate=1.2
        )

    def test_get_exchange_rate_success(self):
        """
        GET /currency/{base_currency}/{target_currency} returns the exchange
        rate for given currencies
        """
        url = reverse('exchange-rate-detail', args=['USD', 'EUR'])
        response = self.client.get(url)
        
        expected_data = ExchangeRateSerializer(self.exchange_rate).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)

    def test_get_exchange_rate_not_found(self):
        """
        API returns code 404 if exchange rate is not in the database
        """
        url = reverse('exchange-rate-detail', args=['JPY', 'EUR'])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {"error": "Exchange rate not found"})

    def test_get_exchange_rate_invalid_currency(self):
        """
        API returns code 404 for non-existent currencies
        """
        url = reverse('exchange-rate-detail', args=['XYZ', 'EUR'])
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
