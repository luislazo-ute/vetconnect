from rest_framework import viewsets
from ..models import Servicio
from ..serializers import ServicioSerializer
from ..permissions import IsAdminOrReadOnly


class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all().order_by('id')
    serializer_class = ServicioSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre']
    filterset_fields = ['is_active']
    ordering_fields = ['nombre', 'precio']
