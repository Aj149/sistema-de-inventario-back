from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from common.models import Canton, Provincia
from rest_framework.response import Response
from common.serializers import CantonSerializer, ProvinciaSerializer
# 4aqui se maneja la logica para el crud

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    
    @action(detail=True, methods=['get'])
    def ciudades(self, request, pk=None):
        # Filtrar cantones por provincia
        ciudades = Canton.objects.filter(provincia_id=pk)
        serializer = CantonSerializer(ciudades, many=True)
        return Response(serializer.data)
    
class CantonViewSet(viewsets.ModelViewSet):
    queryset = Canton.objects.all()
    serializer_class = CantonSerializer
