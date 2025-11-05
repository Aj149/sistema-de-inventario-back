# products/models.py
from django.db import models
from suppliers.models import Supplier

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    suppliers = models.ManyToManyField(Supplier, related_name="products")

    def __str__(self):
        return self.name