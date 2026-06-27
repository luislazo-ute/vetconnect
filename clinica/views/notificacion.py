from rest_framework import viewsets
from ..models import Notificacion
from ..serializers import NotificacionSerializer
from facturacion.permissions import IsAdminOrReadOnly


class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all().order_by('-created_at')
    serializer_class = NotificacionSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['mensaje', 'cliente__user__username']
    filterset_fields = ['cliente', 'tipo', 'leida']
    ordering_fields = ['created_at', 'tipo', 'leida']
