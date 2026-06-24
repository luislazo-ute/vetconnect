from rest_framework import viewsets
from ..models import Producto
from ..serializers import ProductoSerializer
from ..permissions import IsAdminOrReadOnly


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre']
    filterset_fields = ['is_active', 'categoria']
    ordering_fields = ['nombre', 'precio', 'stock']
