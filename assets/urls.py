from django.urls import path

from . import views

urlpatterns = [
    path("wallet/", views.WalletView.as_view(), name="Exchange"),
    path("", views.AssetView.as_view(), name="Exchange"),
    path("deposit/", views.DepositView.as_view(), name="Exchange"),
]