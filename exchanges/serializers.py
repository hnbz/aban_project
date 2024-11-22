from rest_framework import serializers
from .models import Exchange


class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        exclude= ['user']
        read_only_fields = ['status', 'crypto_price_at_the_time', 'created_at', 'updated_at']
