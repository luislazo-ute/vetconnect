from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Veterinario, Mascota, Cita, HistorialMedico


class ClienteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'user', 'username', 'telefono', 'direccion', 'created_at']
        read_only_fields = ['id', 'created_at']

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = ['id', 'user', 'nombre', 'especialidad', 'telefono',
                  'email', 'horario_atencion', 'is_active', 'created_at']
        read_only_fields = ['id', 'created_at']


class MascotaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.user.username', read_only=True)
    especie_display = serializers.CharField(source='get_especie_display', read_only=True)

    class Meta:
        model = Mascota
        fields = ['id', 'nombre', 'especie', 'especie_display', 'raza',
                  'fecha_nacimiento', 'peso', 'cliente', 'cliente_nombre',
                  'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CitaSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)
    estado_display = serializers.CharField(source='get_estado_display', read_only=True)

    class Meta:
        model = Cita
        fields = ['id', 'mascota', 'mascota_nombre', 'veterinario', 'veterinario_nombre',
                  'fecha', 'hora', 'motivo', 'estado', 'estado_display', 'created_at']
        read_only_fields = ['id', 'created_at']

class HistorialMedicoSerializer(serializers.ModelSerializer):
    mascota_nombre = serializers.CharField(source='mascota.nombre', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = HistorialMedico
        fields = ['id', 'mascota', 'mascota_nombre', 'veterinario', 'veterinario_nombre',
                  'fecha', 'diagnostico', 'tratamiento', 'observaciones']
        read_only_fields = ['id', 'fecha']