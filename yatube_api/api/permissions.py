from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Ограничение полного доступа."""
    def has_permission(self, request, view):
        """Разрешает просмотр авторизованным пользователям."""
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Полный доступ для автора."""
        return obj.author == request.user
