from django.db import models
from django.contrib.auth import get_user_model
from aban.base_models import BaseModel
from crypto_currencies.models import CryptoCurrency
from django.core.validators import MinValueValidator


class Wallet(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    balance = models.BigIntegerField(default=0, validators=[MinValueValidator(limit_value=0)])

class Asset(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.RESTRICT)
