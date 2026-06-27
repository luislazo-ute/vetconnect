from django.db import models
from pacientes.models import Mascota, Veterinario, Cita


class Receta(models.Model):
    cita = models.ForeignKey(
        Cita,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recetas',
    )
    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name='recetas',
    )
    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recetas',
    )
    fecha_emision = models.DateTimeField()
    valida_hasta = models.DateField(null=True, blank=True)
    instrucciones = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Receta {self.id} - {self.mascota.nombre} ({self.fecha_emision})'

    class Meta:
        db_table = 'receta'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
