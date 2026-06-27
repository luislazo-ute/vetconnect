from django.db import models
from pacientes.models import Cliente


class Notificacion(models.Model):
    TIPOS = [
        ('recordatorio', 'Recordatorio'),
        ('alerta', 'Alerta'),
        ('informacion', 'Información'),
    ]

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='notificaciones',
    )
    tipo = models.CharField(max_length=20, choices=TIPOS)
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.get_tipo_display()}] {self.cliente.user.username} - {"Leída" if self.leida else "No leída"}'

    class Meta:
        db_table = 'notificacion'
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-created_at']
