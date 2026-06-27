from rest_framework import serializers
from ..models import Hospitalizacion


class HospitalizacionSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    habitacion_numero = serializers.CharField(source='habitacion.numero', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = Hospitalizacion
        fields = ['id', 'mascota', 'mascota_nombre', 'habitacion', 'habitacion_numero',
                  'veterinario', 'veterinario_nombre', 'fecha_ingreso', 'fecha_salida',
                  'motivo', 'diagnostico', 'tratamiento', 'is_active',
                  'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
