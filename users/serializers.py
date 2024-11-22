from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        exclude = ('is_staff', 'is_superuser', ' created_at', 'updated_at')
        model = User
