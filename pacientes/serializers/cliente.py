from rest_framework import serializers
from ..models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'user', 'username', 'telefono', 'direccion', 'created_at']
        read_only_fields = ['id', 'created_at']
