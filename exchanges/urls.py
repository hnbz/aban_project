from django.urls import path

from . import views

urlpatterns = [
    path("", views.ExchangeView.as_view(), name="Exchange"),
]