from posts.models import Comment, Group, Post
from rest_framework import exceptions, viewsets

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class UpdDestrViewSet(viewsets.ModelViewSet):
    """Реализация проверки прав на изменение и удаление чужого контента."""
    def perform_update(self, serializer):
        """Изменение доступно для своего контента."""
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(UpdDestrViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Удаление доступно для своего контента."""
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Удаление чужого контента запрещено!'
            )
        super(UpdDestrViewSet, self).perform_destroy(instance)


class PostViewSet(UpdDestrViewSet):
    """Работа с постами пользователя."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Указание автора для поста при создании."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Просмотр групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(UpdDestrViewSet):
    """Работа с комментариями к постам."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Получение id поста из URL и комментов к нему."""
        post_id = self.kwargs.get('post_id')
        queryset = self.queryset.filter(post=post_id)
        return queryset

    def perform_create(self, serializer):
        """Создание коммента для нужного поста из URL."""
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)
