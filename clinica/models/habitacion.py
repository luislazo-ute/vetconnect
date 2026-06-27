from django.db import models


class Habitacion(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'Mantenimiento'),
    ]

    codigo = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=50, blank=True, default='')
    precio_dia = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    capacidad = models.PositiveIntegerField(default=1)
    observaciones = models.TextField(blank=True, default='')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Habitación {self.codigo} ({self.get_estado_display()})'

    class Meta:
        db_table = 'habitacion'
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'
