from django.db import models
from django.contrib.auth import get_user_model

from aban.base_models import BaseModel
from crypto_currencies.models import CryptoCurrency
# Create your models here.

class Exchange(BaseModel):
    class ExchangeStatusChoice(models.TextChoices):
        PENDING = "pending"
        DONE = "done"
    user = models.ForeignKey(get_user_model(), on_delete=models.RESTRICT)
    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.RESTRICT)
    crypto_price_at_the_time = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    status = models.CharField(choices=ExchangeStatusChoice)
