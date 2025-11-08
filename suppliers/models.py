from django.db import models

from common.models import Canton, Provincia
#  1desde common.models importamos provincias y cantones


# 1creamos el nombre de la tabla que se llamara suppliers
class Supplier(models.Model):
    # 4informacion basica
    # creamos las columnas que tendra nuestra tabla suppliers dandole un nombre, 
    # un el tipo de dato que va a recibir y el maximo de caracteres tambien le decimos que no puede haber 2 proveedores
    nombre_empresa = models.CharField(max_length=255, unique=True)
    nombre_comercial = models.CharField(max_length=255, unique=True)    
    
    # creamos una columna para el tipo de documento que el usuario escoja
    TIPO_DOCUMENTO_CHOICES = [
        ('CEDULA', 'Cédula'),
        ('RUC', 'RUC'),
    ]
    # en el caso de que el usuario no escoja ninguna de las anteriores opciones
    tipo_documento = models.CharField(
        max_length=20,
        choices=TIPO_DOCUMENTO_CHOICES,
        # por defecto se seleccionara cedula
        default='CEDULA'
    )

    numero_documento = models.CharField(
        max_length=20,
        unique=True
    )
    
    # 4Direccion
    
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True)
    canton = models.ForeignKey(Canton, on_delete=models.SET_NULL, null=True, blank=True)
    correo = models.EmailField(max_length=255, unique=True, blank=False)
    direccion = models.TextField(max_length=255)
    telefono = models.CharField(max_length=15)
    
    # 4informacion bancaria
    tipo_banco = models.CharField(max_length=150, null=True)
    tipo_cuenta = models.CharField(max_length=100,null=True, blank=True)
    num_cuenta = models.CharField(max_length=100,null=True, blank=True)
    dueno_cuenta = models.CharField(max_length=250, null=True, blank=True)
    cedula_ruc_dueno = models.CharField(max_length=13, null=True, blank=True)

    rubro = models.CharField(max_length=150, null=True, blank=True)
    estado = models.CharField(max_length=50,null=True, blank=True)
    observaciones = models.CharField(max_length=150,null=True, blank=True)
    
    # 4imagen de la empresa
    imagen = models.ImageField(upload_to='test/', blank=True, null=True)
    
    
    

    def __str__(self):
        return f"{self.tipo_documento}: {self.numero_documento}"

    

