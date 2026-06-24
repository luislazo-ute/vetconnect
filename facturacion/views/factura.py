from rest_framework import viewsets
from ..models import Factura
from ..serializers import FacturaSerializer
from ..permissions import IsAdminOrReadOnly


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all().order_by('id')
    serializer_class = FacturaSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['pagada', 'cliente']
    ordering_fields = ['fecha', 'total']
