from django.db import models

from aban.base_models import BaseModel


# Create your models here.
class CryptoCurrency(BaseModel):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=255, unique=True)
    price_buy = models.DecimalField(max_digits=20, decimal_places=10)
    price_sell = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return f'{self.name} ({self.symbol})'