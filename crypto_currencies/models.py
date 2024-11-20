from django.db import models

from aban.base_models import BaseModel


# Create your models here.
class CryptoCurrency(BaseModel):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
