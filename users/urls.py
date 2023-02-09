from django.urls import include, path, resolve
from wester.utils import get_app_name

from . import views
from .apps import UserConfig

urlpatterns = [
    path('api/' + get_app_name(__package__) + '/', include('users.api.urls')),
]