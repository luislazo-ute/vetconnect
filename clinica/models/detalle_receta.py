from django.db import models
from facturacion.models import Producto
from .receta import Receta


class DetalleReceta(models.Model):
    receta = models.ForeignKey(
        Receta,
        on_delete=models.CASCADE,
        related_name='detalles',
    )
    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name='detalles_receta',
    )
    dosis = models.CharField(max_length=200)
    frecuencia = models.CharField(max_length=200)
    duracion = models.CharField(max_length=200, blank=True, default='')
    observaciones = models.TextField(blank=True, default='')

    def __str__(self):
        return f'{self.producto.nombre} - {self.dosis}'

    class Meta:
        db_table = 'detalle_receta'
        verbose_name = 'Detalle de receta'
        verbose_name_plural = 'Detalles de receta'
