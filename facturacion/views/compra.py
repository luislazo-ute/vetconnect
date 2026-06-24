from rest_framework import viewsets
from ..models import Compra
from ..serializers import CompraSerializer
from ..permissions import IsAdminOrReadOnly


class CompraViewSet(viewsets.ModelViewSet):
    queryset = Compra.objects.all().order_by('id')
    serializer_class = CompraSerializer
    permission_classes = [IsAdminOrReadOnly]
    filterset_fields = ['estado', 'proveedor']
    ordering_fields = ['fecha', 'total']
