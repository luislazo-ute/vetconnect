from django.db import models
from .mascota import Mascota
from .veterinario import Veterinario


class Cita(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='citas',)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.SET_NULL, null=True, related_name='citas',)
    fecha = models.DateTimeField()
    hora = models.TimeField()
    motivo = models.TextField(blank=True, default='')
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.mascota.nombre} - {self.fecha}{self.hora}'

    class Meta:
        db_table = 'cita'
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['-fecha', '-hora']
