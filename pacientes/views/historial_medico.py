from rest_framework import viewsets
from ..models import HistorialMedico
from ..serializers import HistorialMedicoSerializer
from ..permissions import IsAdminOrReadOnly


class HistorialMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistorialMedicoSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['mascota__nombre', 'diagnostico']
    filterset_fields = ['mascota', 'veterinario']
    ordering_fields = ['fecha']
