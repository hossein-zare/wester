from rest_framework.authtoken.models import Token as AuthToken
from django.db import models
from django.conf import settings
from django.utils import timezone

class Token(AuthToken):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=40, db_index=True, unique=True)
    ip = models.CharField(max_length=40)
    data = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True)