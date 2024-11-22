from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from assets.models import Wallet, Asset
from crypto_currencies.models import CryptoCurrency
from exchanges.models import Exchange
from decimal import Decimal

User = get_user_model()

class ExchangeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(mobile="9022222222", password="password")
        self.client.force_authenticate(user=self.user)

        # Get or create Wallet for user
        self.wallet, _ = Wallet.objects.get_or_create(user=self.user, defaults={'balance': Decimal('1000.00')})

        # Set up CryptoCurrency
        self.crypto = CryptoCurrency.objects.create(
            name="Bitcoin",
            symbol="BTC",
            price_buy=Decimal('50.00'),
            price_sell = Decimal('55.00')
        )

        # Base data for creating exchanges
        self.exchange_data = {
            "crypto_currency": self.crypto.id,
            "quantity": Decimal('10.00')
        }

    def test_create_exchange_sufficient_balance(self):
        """Test creating an exchange when the user has sufficient balance."""
        self.wallet.balance = Decimal('1000.00')  # Ensure sufficient balance
        self.wallet.save()
        response = self.client.post('/exchanges/', self.exchange_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify Wallet balance
        self.wallet.refresh_from_db()
        expected_balance = Decimal('1000.00') - (Decimal('10.00') * Decimal('50.00'))
        self.assertEqual(self.wallet.balance, expected_balance)

        # Verify Asset creation
        asset = Asset.objects.filter(user=self.user, crypto_currency=self.crypto).first()
        self.assertIsNotNone(asset)
        self.assertEqual(asset.quantity, Decimal('10.00'))

    def test_create_exchange_insufficient_balance(self):
        """Test creating an exchange when the user has insufficient balance."""
        self.wallet.balance = Decimal('10.00')
        self.wallet.save()

        response = self.client.post('/exchanges/', self.exchange_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('insufficient balance', response.data['detail'])

    def test_signal_batch_processing(self):
        """Test signal for processing pending exchanges."""
        # Create multiple pending exchanges
        self.wallet.balance = Decimal('1000.00')  # Ensure sufficient balance
        self.wallet.save()
        for i in range(3):
            Exchange.objects.create(
                user=self.user,
                crypto_currency=self.crypto,
                crypto_price_at_the_time=self.crypto.price_buy,
                quantity=Decimal('1.00'),
                status=Exchange.ExchangeStatusChoice.PENDING
            )

        # Create a new exchange to trigger the signal
        response = self.client.post('/exchanges/', self.exchange_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify all pending exchanges are processed
        processed_exchanges = Exchange.objects.filter(status=Exchange.ExchangeStatusChoice.DONE)
        self.assertEqual(processed_exchanges.count(), 4)

    def test_asset_update_on_subsequent_exchanges(self):
        """Test updating an existing asset when the user already owns the cryptocurrency."""
        # Create an initial Asset
        self.wallet.balance = Decimal('1000.00')  # Ensure sufficient balance
        self.wallet.save()
        Asset.objects.create(user=self.user, crypto_currency=self.crypto, quantity=Decimal('5.00'))

        response = self.client.post('/exchanges/', self.exchange_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the Asset quantity is updated
        asset = Asset.objects.get(user=self.user, crypto_currency=self.crypto)
        self.assertEqual(asset.quantity, Decimal('15.00'))
