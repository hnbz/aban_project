from django.db.models.signals import post_save
from django.db.models import Sum, F
from django.dispatch import receiver
from .models import Exchange
from .utils import buy_from_exchange, process_exchange


@receiver(post_save, sender=Exchange)
def buy_cumulative_crypto(sender, instance, created, **kwargs):
    if created:
        pending_exchange = Exchange.objects.filter(status=Exchange.ExchangeStatusChoice.PENDING, crypto_currency=instance.crypto_currency)
        pending_exchange_amount = pending_exchange.annotate(sum = Sum(F('crypto_price_at_the_time')*F('quantity'), default=0))['sum']
        if pending_exchange_amount >= 10:
            buy_from_exchange(instance.crypto_currency.symbol, pending_exchange_amount)
            process_exchange(pending_exchange)