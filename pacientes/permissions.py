from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Lectura (GET) para cualquier usuario autenticado.
    Escritura (POST, PUT, DELETE) solo para administradores (is_staff).
    """

    def has_permission(self, request, view):
        # Si el método es de solo lectura (GET, HEAD, OPTIONS), permitir
        if request.method in permissions.SAFE_METHODS:
            return True
        # Para escritura, solo si es staff (admin)
        return request.user and request.user.is_staff
