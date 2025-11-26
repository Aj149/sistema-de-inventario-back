# suppliers/serializers.py
from rest_framework import serializers
from .models import Supplier


class ImageOrURLField(serializers.ImageField):
    """
    Acepta tanto un archivo (upload) como un string (URL S3).
    """
    def to_internal_value(self, data):
        # Caso: llega un string (URL actual)
        if isinstance(data, str):
            return data  
        # Caso: llega un archivo → validar normal
        return super().to_internal_value(data)


class SupplierSerializer(serializers.ModelSerializer):
    provincia_nombre = serializers.CharField(source='provincia.nombre', read_only=True)
    canton_nombre = serializers.CharField(source='canton.nombre', read_only=True)

    # 🔥 CAMBIADO: antes era serializers.ImageField
    imagen = ImageOrURLField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Supplier
        fields = '__all__'

    def update(self, instance, validated_data):
        imagen = validated_data.get('imagen')

        # Caso: llega string → no modificar imagen
        if isinstance(imagen, str):
            validated_data.pop('imagen', None)

        return super().update(instance, validated_data)
