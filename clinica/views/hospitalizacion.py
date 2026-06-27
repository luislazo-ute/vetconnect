from rest_framework import viewsets
from ..models import Hospitalizacion
from ..serializers import HospitalizacionSerializer
from ..permissions import IsAdminOrReadOnly


class HospitalizacionViewSet(viewsets.ModelViewSet):
    queryset = Hospitalizacion.objects.all().order_by('-fecha_ingreso')
    serializer_class = HospitalizacionSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['motivo', 'mascota__nombre', 'diagnostico']
    filterset_fields = ['mascota', 'habitacion', 'veterinario', 'is_active']
    ordering_fields = ['fecha_ingreso', 'fecha_alta']
