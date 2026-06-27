from django.db import models
from pacientes.models import Mascota, Veterinario
from .habitacion import Habitacion


class Hospitalizacion(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='hospitalizaciones',
    )
    habitacion = models.ForeignKey(
        Habitacion,
        on_delete=models.PROTECT,
        related_name='hospitalizaciones',
    )
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='hospitalizaciones',
    )
    fecha_ingreso = models.DateTimeField()
    fecha_alta = models.DateTimeField(null=True, blank=True)
    motivo = models.TextField()
    diagnostico = models.TextField(blank=True, default='')
    tratamiento = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.mascota.nombre} - {self.habitacion.codigo} ({self.fecha_ingreso.date()})'

    class Meta:
        db_table = 'hospitalizacion'
        verbose_name = 'Hospitalización'
        verbose_name_plural = 'Hospitalizaciones'
