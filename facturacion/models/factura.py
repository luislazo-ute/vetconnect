from django.db import models
from pacientes.models import Cliente


class Factura(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='facturas',
    )
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f'Factura {self.id} - {self.cliente.user.username}'

    class Meta:
        db_table = 'factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
        ordering = ['-fecha']
