from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешает читать объект любому, а редактировать только его автору.
    """
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsOwner(permissions.BasePermission):
    """
    Разрешает доступ только владельцу объекта.
    """
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAuthenticatedAndActive(permissions.BasePermission):
    """
    Разрешает доступ только аутентифицированным активным пользователям.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_active