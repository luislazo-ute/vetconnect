from django.db import models
from pacientes.models import Mascota, Veterinario


class Vacuna(models.Model):
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='vacunas',
    )
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='vacunas_aplicadas',
    )
    nombre_vacuna = models.CharField(max_length=100)
    fecha_aplicacion = models.DateField()
    fecha_proxima_dosis = models.DateField(null=True, blank=True)
    lote = models.CharField(max_length=50, blank=True, default='')
    observaciones = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre_vacuna} - {self.mascota.nombre} ({self.fecha_aplicacion})'

    class Meta:
        db_table = 'vacuna'
        verbose_name = 'Vacuna'
        verbose_name_plural = 'Vacunas'
