from rest_framework import viewsets
from ..models import Mascota
from ..serializers import MascotaSerializer
from ..permissions import IsAdminOrReadOnly


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre', 'raza']
    filterset_fields = ['especie', 'is_active', 'cliente']
    ordering_fields = ['nombre', 'created_at']
