from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.Register.as_view(), name="Register"),
    path("login/", views.Login.as_view(), name="login")
]