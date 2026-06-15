from rest_framework import viewsets
from ..models import Cliente
from ..serializers import ClienteSerializer
from ..permissions import IsAdminOrReadOnly


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = ClienteSerializer
    permission_classes = [IsAdminOrReadOnly]
    search_fields = ['user__username', 'telefono']
    filterset_fields = ['user']
    ordering_fields = ['created_at', 'id']
