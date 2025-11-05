from django.db import models
# 1creamos una tabla de nombre provincia
class Provincia(models.Model):
    # 1luego le damos una columna que se llama nombre
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
# 1creamos otra tabla de cantones
class Canton (models.Model):
    # 1creamos una columna nombre
    nombre = models.CharField(max_length=50)
    # 1le damos el nombre de provincia dentro de la tabla cantones porque es ahi donde se va a guardar las forenkey de las provincias
    provincia= models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='canton')
    
    def __str__(self):
        return self.nombre