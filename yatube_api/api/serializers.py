from posts.models import Comment, Group, Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """Сериализация постов."""
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('__all__')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализация групп."""

    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Сериализация комментариев."""
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ('__all__')
        model = Comment
        read_only_fields = ('post',)
