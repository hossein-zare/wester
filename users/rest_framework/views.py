from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from wester.rest_framework.permissions import IsGuest
from .serializers import UserSerializer

@api_view()
@permission_classes([IsGuest])
def register(request):
    serializer = UserSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors)

    return Response(serializer.validated_data)