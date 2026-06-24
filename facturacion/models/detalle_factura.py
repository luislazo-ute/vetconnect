from django.db import models
from .factura import Factura
from .servicio import Servicio


class DetalleFactura(models.Model):
    factura = models.ForeignKey(
        Factura,
        on_delete=models.CASCADE,
        related_name='detalles',
    )
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.PROTECT,
        related_name='detalles_factura',
    )
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f'{self.servicio.nombre} x {self.cantidad}'

    class Meta:
        db_table = 'detalle_factura'
        verbose_name = 'Detalle de Factura'
        verbose_name_plural = 'Detalles de Factura'
