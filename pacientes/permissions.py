from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Lectura (GET) para cualquier usuario autenticado.
    Escritura (POST, PUT, DELETE) solo para administradores (is_staff).
    """

    def has_permission(self, request, view):
        # Sin usuario autenticado no se permite nada (ni lectura).
        if not (request.user and request.user.is_authenticated):
            return False
        # Lectura (GET, HEAD, OPTIONS) para cualquier usuario autenticado.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Escritura solo para staff (admin).
        return request.user.is_staff
