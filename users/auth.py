from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

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
    data = {}

    return Token.objects.create(user=user, data=json.dumps(data), ip='127.0.0.1')