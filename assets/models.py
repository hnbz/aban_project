from django.db import models
from django.contrib.auth import get_user_model
from aban.base_models import BaseModel
from crypto_currencies.models import CryptoCurrency
from django.core.validators import MinValueValidator


class Wallet(BaseModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=10)

class Asset(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=20, decimal_places=8, default=0)
    crypto_currency = models.ForeignKey(CryptoCurrency, on_delete=models.RESTRICT)

class Deposit(BaseModel):
    wallet = models.ForeignKey(Wallet, on_delete=models.RESTRICT)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    before_balance = models.DecimalField(max_digits=20, decimal_places=10)
    after_balance = models.DecimalField(max_digits=20, decimal_places=10)