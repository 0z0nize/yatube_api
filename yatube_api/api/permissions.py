# Для проверки прав в DRF удобно использовать пермишены.
# При необходимости пишите и применяйте собственные классы разрешений.
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.author == request.user
            or request.method in permissions.SAFE_METHODS
        )
