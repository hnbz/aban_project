from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.db import transaction
from rest_framework.exceptions import APIException
from assets.models import Wallet, Asset, Deposit
from assets.serializers import AssetSerializer, DepositSerializer, WalletSerializer
from rest_framework.response import Response


class DepositView(ListCreateAPIView):
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: DepositSerializer):
        user = self.request.user
        if not user.is_verified:
            raise APIException(detail='verification required', code=status.HTTP_400_BAD_REQUEST)
        data: dict = serializer.validated_data
        with transaction.atomic():
            wallet = Wallet.objects.filter(user=user).first()
            after_balance = wallet.balance + data.get('amount')
            serializer.save(wallet=wallet, before_balance=wallet.balance, after_balance=after_balance)
            wallet.balance = after_balance
            wallet.save()
            return Response(status.HTTP_201_CREATED)

    def get_queryset(self):
        wallet = Wallet.objects.filter(user=self.request.user).first()
        return Deposit.objects.filter(wallet=wallet).all()
