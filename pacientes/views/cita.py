from rest_framework import viewsets, filters
from ..models import Cita
from ..serializers import CitaSerializer
from ..permissions import IsAdminOrReadOnly


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['mascota__nombre', 'motivo']
