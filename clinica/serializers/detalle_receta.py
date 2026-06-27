from rest_framework import serializers
from ..models import DetalleReceta


class DetalleRecetaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetalleReceta
        fields = ['id', 'receta', 'producto', 'producto_nombre',
                  'dosis', 'frecuencia', 'duracion', 'observaciones']
        read_only_fields = ['id']
