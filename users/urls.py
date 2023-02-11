from django.urls import include, path, resolve

from wester.utils import get_app_name

urlpatterns = [
    path('api/' + get_app_name(__package__) + '/', include('users.rest_framework.urls')),
]