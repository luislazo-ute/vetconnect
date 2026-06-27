from rest_framework import serializers
from ..models import Habitacion


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = ['id', 'codigo', 'tipo', 'precio_dia', 'estado', 'capacidad',
                  'observaciones', 'is_active']
        read_only_fields = ['id']
