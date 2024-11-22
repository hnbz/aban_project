from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.authtoken.models import Token
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import APIException


# Create your views here.
class Register(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer: UserSerializer):
        if User.objects.filter(mobile = serializer.validated_data.get('mobile')):
            raise APIException(detail='user with this mobile number already exists', code=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class Login(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['mobile'], password=serializer.validated_data['password'])
        if user:
            token, token_status = Token.objects.get_or_create(user=user)
            return Response(data = {"token": token.key}, status=201 if token_status else 200)
        raise APIException(detail='Invalid credential', code=status.HTTP_401_UNAUTHORIZED)