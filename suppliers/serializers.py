# suppliers/serializers.py
from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    provincia = serializers.CharField(source='provincia.nombre', read_only=True)
    canton = serializers.CharField(source='canton.nombre', read_only=True)
    class Meta:
        model = Supplier
        fields = '__all__'
        
