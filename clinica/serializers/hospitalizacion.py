from rest_framework import serializers
from ..models import Hospitalizacion


class HospitalizacionSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    habitacion_codigo = serializers.CharField(source='habitacion.codigo', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = Hospitalizacion
        fields = ['id', 'mascota', 'mascota_nombre', 'habitacion', 'habitacion_codigo',
                  'veterinario', 'veterinario_nombre', 'fecha_ingreso', 'fecha_alta',
                  'motivo', 'diagnostico', 'tratamiento', 'is_active',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
