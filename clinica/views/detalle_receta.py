from rest_framework import viewsets
from ..models import DetalleReceta
from ..serializers import DetalleRecetaSerializer
from ..permissions import IsAdminOrReadOnly


class DetalleRecetaViewSet(viewsets.ModelViewSet):
    queryset = DetalleReceta.objects.all().order_by('id')
    serializer_class = DetalleRecetaSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['dosis', 'frecuencia', 'producto__nombre']
    filterset_fields = ['receta', 'producto']
    ordering_fields = ['id']
