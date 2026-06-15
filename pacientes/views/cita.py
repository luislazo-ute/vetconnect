from rest_framework import viewsets
from ..models import Cita
from ..serializers import CitaSerializer
from ..permissions import IsAdminOrReadOnly


class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['mascota__nombre', 'motivo']
    filterset_fields = ['estado', 'mascota', 'veterinario']
    ordering_fields = ['fecha', 'hora', 'created_at']
