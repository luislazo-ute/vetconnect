from rest_framework import viewsets
from ..models import Pago
from ..serializers import PagoSerializer
from ..permissions import IsAdminOrReadOnly


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all().order_by('id')
    serializer_class = PagoSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['factura', 'metodo_pago']
    ordering_fields = ['fecha_pago', 'monto']
