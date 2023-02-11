from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from operator import itemgetter
from django.utils import timezone

from wester.rest_framework.permissions import IsGuest
from wester.utils import get_client_ip_address
from .serializers import RegisterSerializer, LoginSerializer
from ..models import User
from .auth import create_token

@api_view(['POST'])
@permission_classes([IsGuest])
def register(request):
    serializer = RegisterSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors)

    user = User.objects.create_user(**serializer.validated_data)
    token = create_token(request, user).key

    return Response({
        'token': key
    })

@api_view(['POST'])
@permission_classes([IsGuest])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors)

    token = create_token(request, serializer.user).key

    return Response({
        'token': token
    })

@api_view(['DELETE'])
def logout(request):
    request.auth.deleted_at = timezone.now()
    request.auth.save()

    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def auth(request):
    return Response({
        'id': request.user.id,
        'name': request.user.name,
        'username': request.user.username,
    })