from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from wester.rest_framework.permissions import IsGuest

@api_view()
@permission_classes([IsGuest])
def register(request):
    return Response({
        'name': 'hossein'
    })