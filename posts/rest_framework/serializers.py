from rest_framework import serializers

from ..models import Post

class PostSerializer(serializers.Serializer):
    """
    Create and update a post.
    """

    content = serializers.CharField(min_length=1, max_length=1024)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

    def to_representation(self, instance):
        return {
            'id': str(instance.id),
            'user_id': str(instance.user_id),
            'content': instance.content,
            'created_at': instance.created_at,
        }