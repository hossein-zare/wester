from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from wester.fields import UnsignedAutoField

class User(AbstractBaseUser):
    id = UnsignedAutoField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    mobile_number = models.EmailField(unique=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_restricted = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.name or self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin