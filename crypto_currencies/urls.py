from django.urls import path, include
from rest_framework import routers
from .views import CryptoViewSet

router = routers.DefaultRouter()
router.register(r'crypto_currencies', CryptoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]