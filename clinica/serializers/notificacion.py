from rest_framework import serializers
from ..models import Notificacion


class NotificacionSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.CharField(source='cliente.user.username', read_only=True)

    class Meta:
        model = Notificacion
        fields = ['id', 'cliente', 'cliente_nombre', 'tipo', 'titulo', 'mensaje',
                  'leida', 'created_at']
        read_only_fields = ['id', 'created_at']
