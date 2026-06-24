from rest_framework import serializers
from ..models import DetalleFactura


class DetalleFacturaSerializer(serializers.ModelSerializer):
    servicio_nombre = serializers.CharField(source='servicio.nombre', read_only=True)

    class Meta:
        model = DetalleFactura
        fields = ['id', 'factura', 'servicio', 'servicio_nombre',
                  'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['id']
