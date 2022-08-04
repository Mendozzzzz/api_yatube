from rest_framework import serializers
from posts.models import Post, User
from django.shortcuts import render, get_object_or_404


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )


    class Meta:
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post

