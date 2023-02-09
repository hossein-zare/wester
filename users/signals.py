from django.db.models.signals import post_save
from django.conf import settings

# Example:
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_token():
#     pass