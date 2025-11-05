from django.shortcuts import render
from rest_framework import viewsets
from common.models import Canton, Provincia
from common.serializers import CantonSerializer, ProvinciaSerializer
# 4aqui se maneja la logica para el crud

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    
class CantonViewSet(viewsets.ModelViewSet):
    queryset = Canton.objects.all()
    serializer_class = CantonSerializer
