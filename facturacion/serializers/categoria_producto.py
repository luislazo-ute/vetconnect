from rest_framework import serializers
from ..models import CategoriaProducto


class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        read_only_fields = ['id']
