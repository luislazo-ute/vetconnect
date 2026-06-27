from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Lectura para cualquier usuario autenticado.
    Escritura (POST, PUT, PATCH, DELETE) solo para staff.
    """

    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
