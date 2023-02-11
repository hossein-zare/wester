from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings

from .models import Permission

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_permissions(sender, instance=None, created=False, **kwargs):
    """
    Create a permission record for user on creation.
    """

    if created:
        Permission.objects.create(user=instance)