from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils import timezone

from .managers import UserManager

class User(AbstractBaseUser):
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=12, unique=True, null=True)
    profile_picture = models.CharField(max_length=100, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_restricted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.name or self.username

class Permission(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    create_post = models.BooleanField(default=True)