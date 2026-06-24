from rest_framework import viewsets
from ..models import Proveedor
from ..serializers import ProveedorSerializer
from ..permissions import IsAdminOrReadOnly


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all().order_by('id')
    serializer_class = ProveedorSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre', 'contacto']
    filterset_fields = ['is_active']
    ordering_fields = ['nombre']
