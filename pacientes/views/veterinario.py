from rest_framework import viewsets
from ..models import Veterinario
from ..serializers import VeterinarioSerializer
from ..permissions import IsAdminOrReadOnly


class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['nombre', 'especialidad']
    filterset_fields = ['especialidad', 'is_active']
    ordering_fields = ['nombre', 'created_at']
