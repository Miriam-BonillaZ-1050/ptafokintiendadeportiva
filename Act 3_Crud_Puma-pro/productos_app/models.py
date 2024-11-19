from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=8)
    nombre_p = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
