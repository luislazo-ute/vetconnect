from rest_framework import viewsets, filters
from ..models import HistorialMedico
from ..serializers import HistorialMedicoSerializer
from ..permissions import IsAdminOrReadOnly


class HistorialMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistorialMedicoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['mascota__nombre', 'diagnostico']
