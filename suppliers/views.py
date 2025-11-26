from django.shortcuts import render
# 4aqui se maneja la logica para el crud
# suppliers/views.py
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from .models import Supplier
from .serializers import SupplierSerializer
from rest_framework import permissions
from rest_framework.parsers import JSONParser


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser, JSONParser]