import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class UsernameValidator:
    message = _('This field is invalid.')
    requires_context = True

    def __init__(self, message=None):
        self.message = message or self.message

    def __call__(self, value, serializer_field):
        if not re.match("^[a-zA-Z0-9_.-]+$", value):
            raise ValidationError(self.message)