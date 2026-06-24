from rest_framework import serializers
from ..models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock',
                  'categoria', 'categoria_nombre', 'is_active']
        read_only_fields = ['id']
