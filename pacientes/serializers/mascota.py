from rest_framework import serializers
from ..models import Mascota


class MascotaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.user.username', read_only=True)
    especie_display = serializers.CharField(source='get_especie_display', read_only=True)

    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'especie', 'especie_display', 'raza',
                  'fecha_nacimiento', 'peso', 'cliente', 'cliente_nombre',
                  'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
