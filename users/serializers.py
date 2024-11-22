from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        fields = ['mobile', 'password']
        model = User

class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField(required=True, max_length=10, min_length=10)
    password = serializers.CharField(required=True, min_length=6)