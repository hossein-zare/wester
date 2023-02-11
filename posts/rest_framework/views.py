from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from users.rest_framework.permissions import CanUser
from ..models import Post

class Posts(APIView):
    permission_classes = [CanUser('create_post', methods=['POST'])]

    def get(self, request, id):
        """
        Read a post.
        """

        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def post(self, request):
        """
        Create a new post.
        """

        serializer = PostSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save(user=request.user)

        return Response(serializer.data)