from rest_framework import serializers
from ..models import Receta


class RecetaSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = Receta
        fields = ['id', 'cita', 'mascota', 'mascota_nombre', 'veterinario',
                  'veterinario_nombre', 'fecha_emision', 'valida_hasta',
                  'instrucciones', 'created_at']
        read_only_fields = ['id', 'created_at']
