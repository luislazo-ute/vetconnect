from rest_framework import viewsets
from ..models import Vacuna
from ..serializers import VacunaSerializer
from ..permissions import IsAdminOrReadOnly


class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all().order_by('-fecha_aplicacion')
    serializer_class = VacunaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre_vacuna', 'mascota__nombre', 'lote']
    filterset_fields = ['mascota', 'veterinario']
    ordering_fields = ['fecha_aplicacion', 'nombre_vacuna']
