from rest_framework import serializers
from ..models import Veterinario


class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['id', 'user', 'nombre', 'especialidad', 'telefono',
                  'email', 'horario_atencion', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']
