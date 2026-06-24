from rest_framework import viewsets
from ..models import CategoriaProducto
from ..serializers import CategoriaProductoSerializer
from ..permissions import IsAdminOrReadOnly


class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all().order_by('id')
    serializer_class = CategoriaProductoSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre']
    filterset_fields = ['is_active']
