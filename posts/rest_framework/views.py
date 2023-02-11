from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .serializers import PostSerializer
from users.permissions import CanUser

@api_view(['POST'])
@permission_classes([CanUser('create_post')])
def create(request):
    """
    Create a new post.
    """

    serializer = PostSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors)

    serializer.save(user=request.user)

    return Response(serializer.data)