from rest_framework import serializers
from ..models import Compra


class CompraSerializer(serializers.ModelSerializer):
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', read_only=True)

    class Meta:
        model = Compra
        fields = ['id', 'proveedor', 'proveedor_nombre', 'fecha_compra',
                  'numero_factura', 'total', 'estado']
        read_only_fields = ['id', 'fecha_compra']
