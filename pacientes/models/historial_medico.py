from django.db import models
from .mascota import Mascota
from .veterinario import Veterinario


class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='historiales',)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, related_name='historiales',)
    fecha = models.DateTimeField(auto_now_add=True)
    diagnostico = models.TextField()
    tratamiento = models.TextField(blank=True, default='')
    observaciones = models.TextField(blank=True, default='')

    def __str__(self):
        return f'{self.mascota.nombre} - {self.fecha.date()}'

    class Meta:
        db_table = 'historial_medico'
        verbose_name = 'Historial Médico'
        verbose_name_plural = 'Historiales Médicos'
        ordering = ['-fecha']
