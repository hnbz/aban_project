from rest_framework import serializers
from .models import Wallet, Asset, Deposit


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance']
