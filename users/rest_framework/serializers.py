from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from wester.validators import UsernameValidator
from ..models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, allow_blank=True)
    username = serializers.CharField(min_length=3, max_length=30, validators=[
        UsernameValidator(message='The username is invalid.'),
        UniqueValidator(
            queryset=User.objects.all(),
            message='The username is already in user.'
        )
    ])
    email = serializers.EmailField(validators=[
        UniqueValidator(
            queryset=User.objects.all(),
            message='The email address is already in user.'
        )
    ])
    password = serializers.CharField(write_only=True)