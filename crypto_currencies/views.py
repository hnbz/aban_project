from rest_framework import viewsets

from .permissions import IsSuperUserOrReadOnly
from .serializers import CryptocurrencySerializer
from .models import CryptoCurrency

class CryptoViewSet(viewsets.ModelViewSet):
    queryset = CryptoCurrency.objects.all()
    serializer_class = CryptocurrencySerializer
    permission_classes = [IsSuperUserOrReadOnly]