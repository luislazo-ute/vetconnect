from rest_framework import viewsets, filters
from ..models import Cliente
from ..serializers import ClienteSerializer
from ..permissions import IsAdminOrReadOnly


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'telefono']
