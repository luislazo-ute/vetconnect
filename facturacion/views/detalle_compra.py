from rest_framework import viewsets
from ..models import DetalleCompra
from ..serializers import DetalleCompraSerializer
from ..permissions import IsAdminOrReadOnly


class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all().order_by('id')
    serializer_class = DetalleCompraSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['compra', 'producto']
