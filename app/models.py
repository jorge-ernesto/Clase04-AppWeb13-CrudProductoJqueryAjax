from django.db import models

# Create your models here.
 
class Producto(models.Model):
    #constantes
    BEBIDAS = 1
    DULCES = 2
    LACTEOS = 3

    CATEGORIAS = (
        (BEBIDAS, 'Bebidas'),
        (DULCES, 'Dulces'),
        (LACTEOS, 'Lacteos'),
    )
    
    nombre = models.CharField(max_length=30)
    fecha = models.DateField(blank=True, null=True)
    categoria = models.PositiveSmallIntegerField(choices=CATEGORIAS, blank=True, null=True)
    codigo = models.CharField(max_length=5, blank=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField(blank=True, null=True)
       
    class Meta:  
        db_table = "productos"
        
    def __str__(self):
        fila=self.nombre+"  "+ self.codigo
        return fila
