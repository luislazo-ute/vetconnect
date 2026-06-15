from rest_framework import serializers
from ..models import HistorialMedico


class HistorialMedicoSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = HistorialMedico
        fields = ['id', 'mascota', 'mascota_nombre', 'veterinario', 'veterinario_nombre',
                  'fecha', 'diagnostico', 'tratamiento', 'observaciones']
        read_only_fields = ['id', 'fecha']
