from rest_framework import viewsets
from ..models import Receta
from ..serializers import RecetaSerializer
from ..permissions import IsAdminOrReadOnly


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('-fecha_emision')
    serializer_class = RecetaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['instrucciones', 'mascota__nombre']
    filterset_fields = ['cita', 'mascota', 'veterinario', 'fecha_emision']
    ordering_fields = ['fecha_emision']
