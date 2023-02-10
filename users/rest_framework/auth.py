from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils.crypto import get_random_string
import json

from wester.utils import get_client_ip_address
from .models import Token

class CustomTokenAuthentication(TokenAuthentication):
    model = Token

    def authenticate_credentials(self, key, request=None):
        try:
            token = self.model.objects.select_related('user').get(key=key)
        except self.model.DoesNotExist:
            raise AuthenticationFailed({
                'error': 'Invalid or Inactive Token',
                'is_authenticated': False
            })
 
        if not token.deleted_at == None or not token.user.is_active:
            raise AuthenticationFailed({
                'error': 'Invalid user',
                'is_authenticated': False
            })

        return token.user, token

def create_token(request, user):
    key = get_random_string(100)
    data = {}
    ip = get_client_ip_address(request)

    return Token.objects.create(user=user, key=key, data=json.dumps(data), ip=ip)