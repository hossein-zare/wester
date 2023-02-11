from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from rest_framework.authtoken import views
from django.contrib.auth.hashers import check_password

from wester.validators import UsernameValidator
from ..models import User

class RegisterSerializer(serializers.Serializer):
    """
    Validate registration data.
    """

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

class LoginSerializer(serializers.Serializer):
    """
    Validate login data.
    """

    username = serializers.CharField(min_length=3, max_length=30, validators=[
        UsernameValidator(message='The username is invalid.'),
    ])
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()

        if user and check_password(attrs['password'], user.password):
            self.user = user
        else:
            raise ValidationError({ 'username': 'Username or password was wrong.' })

        return attrs

class PermissionSerializer(serializers.BaseSerializer):
    """
    Present permissions.
    """

    def to_representation(self, instance):
        return {
            'can_add_post': instance.can_add_post,
        }

class AuthSerializer(serializers.BaseSerializer):
    """
    Present the insensitive auth data.
    """

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'username': instance.username,
            'profile_picture': instance.profile_picture,
            'permissions': PermissionSerializer(instance.permission).data
        }