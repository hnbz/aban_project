from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from assets.models import Wallet, Asset
from crypto_currencies.models import CryptoCurrency
from exchanges.models import Exchange
from exchanges.serializers import ExchangeSerializer
from aban.exceptions import BadRequest
from rest_framework import status
from django.db import transaction


# Create your views here.
class ExchangeView(ListCreateAPIView):
    serializer_class = ExchangeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: ExchangeSerializer):
        crypto = get_object_or_404(CryptoCurrency, pk=serializer.validated_data.get('crypto_currency').id)
        wallet = Wallet.objects.filter(user=self.request.user).first()
        volume = serializer.validated_data.get('quantity') * crypto.price_buy
        if wallet.balance < volume:
            raise BadRequest(detail='insufficient balance', code=status.HTTP_400_BAD_REQUEST)
        with transaction.atomic():
            serializer.save(user=self.request.user, crypto_price_at_the_time=crypto.price_buy)
            wallet.balance -= volume
            wallet.save()
            asset = Asset.objects.filter(user=self.request.user, crypto_currency=crypto).first()
            if asset is None:
                asset = Asset.objects.create(user=self.request.user, crypto_currency=crypto, quantity=serializer.validated_data.get('quantity'))
            else:
                asset.quantity += serializer.validated_data.get('quantity')
                asset.save()

    def get_queryset(self):
        return Exchange.objects.filter(user=self.request.user).all()

