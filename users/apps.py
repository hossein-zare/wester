from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'wester.models.UnsignedBigAutoField'
    name = 'users'

    def ready(self):
        from . import signals