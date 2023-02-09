from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.conf import settings
from rest_framework.authtoken.models import Token as AuthToken

from .managers import UserManager

class User(AbstractBaseUser):
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=12, unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
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

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

class Token(AuthToken):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=40, db_index=True, unique=True)
    ip = models.CharField(max_length=40)
    data = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)