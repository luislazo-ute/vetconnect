from rest_framework import viewsets
from ..models import Habitacion
from ..serializers import HabitacionSerializer
from facturacion.permissions import IsAdminOrReadOnly


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all().order_by('numero')
    serializer_class = HabitacionSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['numero', 'tipo']
    filterset_fields = ['estado']
    ordering_fields = ['numero', 'precio_dia', 'estado']
