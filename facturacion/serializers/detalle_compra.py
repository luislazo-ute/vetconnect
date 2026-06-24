from rest_framework import serializers
from ..models import DetalleCompra


class DetalleCompraSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetalleCompra
        fields = ['id', 'compra', 'producto', 'producto_nombre',
                  'cantidad', 'precio_unitario', 'subtotal']
        read_only_fields = ['id']
