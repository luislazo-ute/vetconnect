from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from ..serializers import (
    UserSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """CRUD de usuarios para administradores, con acciones de perfil propio."""
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        # profile y change-password los usa el propio usuario autenticado.
        if self.action in ('profile', 'change_password'):
            return [IsAuthenticated()]
        return super().get_permissions()

    @action(detail=False, methods=['get', 'patch'], url_path='profile')
    def profile(self, request):
        if request.method.lower() == 'patch':
            serializer = UserProfileSerializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], url_path='change-password')
    def change_password(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        user = request.user
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        return Response(
            {'mensaje': 'Contraseña actualizada correctamente.'},
            status=status.HTTP_200_OK,
        )
