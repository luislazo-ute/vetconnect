from rest_framework import viewsets
from ..models import Habitacion
from ..serializers import HabitacionSerializer
from ..permissions import IsAdminOrReadOnly


class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all().order_by('codigo')
    serializer_class = HabitacionSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['codigo', 'tipo']
    filterset_fields = ['estado', 'is_active']
    ordering_fields = ['codigo', 'precio_dia', 'estado']
