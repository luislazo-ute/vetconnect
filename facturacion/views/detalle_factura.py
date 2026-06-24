from rest_framework import viewsets
from ..models import DetalleFactura
from ..serializers import DetalleFacturaSerializer
from ..permissions import IsAdminOrReadOnly


class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all().order_by('id')
    serializer_class = DetalleFacturaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['factura', 'servicio']
