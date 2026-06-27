from django.db import models
from pacientes.models import Mascota, Veterinario


class Receta(models.Model):
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
    fecha = models.DateField()
    instrucciones = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Receta {self.id} - {self.mascota.nombre} ({self.fecha})'

    class Meta:
        db_table = 'receta'
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
