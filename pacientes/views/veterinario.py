from rest_framework import viewsets, filters
from ..models import Veterinario
from ..serializers import VeterinarioSerializer
from ..permissions import IsAdminOrReadOnly


class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'especialidad']
