from rest_framework import serializers
from ..models import Vacuna


class VacunaSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = Vacuna
        fields = ['id', 'mascota', 'mascota_nombre', 'veterinario', 'veterinario_nombre',
                  'nombre', 'fecha_aplicacion', 'fecha_proxima', 'lote',
                  'observaciones', 'created_at']
        read_only_fields = ['id', 'created_at']
