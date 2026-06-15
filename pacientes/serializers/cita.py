from rest_framework import serializers
from ..models import Cita


class CitaSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Cita
        fields = ['id', 'mascota', 'mascota_nombre', 'veterinario', 'veterinario_nombre',
                  'fecha', 'hora', 'motivo', 'estado', 'estado_display', 'created_at']
        read_only_fields = ['id', 'created_at']
