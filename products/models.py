from django.db import models
from suppliers.models import Supplier

class Product(models.Model):
    codigo = models.CharField(max_length=25, unique=True)
    rubro = models.CharField(max_length=250)
    name = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField(default=0)

    ESTADO_CHOICES = [
    ("NORMAL", "Normal"),
    ("BAJO", "Bajo"),
    ("VACIO", "Sin Stock"),
    ]
    estado = models.CharField(max_length=20,choices=ESTADO_CHOICES,default="NORMAL")
    # imagen al S3
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    suppliers = models.ManyToManyField(Supplier, related_name="products")

    def __str__(self):
        return self.name
