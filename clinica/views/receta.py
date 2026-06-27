from rest_framework import viewsets
from ..models import Receta
from ..serializers import RecetaSerializer
from facturacion.permissions import IsAdminOrReadOnly


class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all().order_by('-fecha')
    serializer_class = RecetaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['instrucciones', 'mascota__nombre']
    filterset_fields = ['mascota', 'veterinario', 'fecha']
    ordering_fields = ['fecha']
