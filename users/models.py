from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, mobile: str, password: str = None, **extra_fields):
        if not mobile:
            raise ValueError("The mobile field is required.")

        email = extra_fields.get('email')
        if email:
            extra_fields['email'] = self.normalize_email(email)

        user = self.model(mobile=mobile, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile: str, password: str = None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        email = extra_fields.get('email')
        if not email:
            raise ValueError("The email field is required.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")
        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(mobile=mobile, password=password, **extra_fields)


class User(AbstractUser):
    mobile = models.CharField(max_length=10, unique=True)
    national_code = models.CharField(max_length=10, unique=True, null=True)
    email = models.EmailField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'mobile'
    username = None

    @property
    def is_verified(self):
        return all([bool(self.national_code), bool(self.email)])

    def str(self):
        return f"{self.first_name} {self.last_name}"