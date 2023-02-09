from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from users.models import Token

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