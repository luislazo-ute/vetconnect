from rest_framework import viewsets, filters
from ..models import Mascota
from ..serializers import MascotaSerializer
from ..permissions import IsAdminOrReadOnly


class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'raza']
