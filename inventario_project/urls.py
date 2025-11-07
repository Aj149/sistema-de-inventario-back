"""
URL configuration for inventario_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from common.views import CantonViewSet, ProvinciaViewSet

from products.views import ProductViewSet
from suppliers.views import SupplierViewSet

# 4esta parte le da la instruccion de crear una ruta a partir de lo que diga Viewset
router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'provincias', ProvinciaViewSet)
router.register(r'ciudades', CantonViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    
# lo que hace es que le dice q dentro de router.urls busque entre product, provincias, suppliers etc.. y que complete en api/
    path('', include(router.urls)),
]

