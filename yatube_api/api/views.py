from django import urls
from rest_framework import viewsets
from posts.models import Post, User
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    # def perform_update(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise Exception('Изменение чужого контента запрещено!')
    #     super(PostViewSet, self).perform_update(serializer)
