from rest_framework import serializers
from ..models import Factura


class FacturaSerializer(serializers.ModelSerializer):
    cliente_username = serializers.CharField(source='cliente.user.username', read_only=True)

    class Meta:
        model = Factura
        fields = ['id', 'cliente', 'cliente_username', 'fecha', 'total', 'pagada']
        read_only_fields = ['id', 'fecha']
