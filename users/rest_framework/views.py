from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from operator import itemgetter

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